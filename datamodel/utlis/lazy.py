"""
This script checks the device schema in the parent folder.
In addition, the color of each device can be specified using the color template. 
Note that devices assigned to a parent device have the same color, 
which is usually darker than the color of the parent device.
"""


import json
import re
import os
from typing import Final
from collections import defaultdict
import pandas as pd
import numpy as np
import yaml
from loguru import logger


logger.remove()
logger.add("lazy.log", format="{time}-{message}")

DEVICE_ROLE: Final[str] = 'device_roles.yml'
COLOR_TEMPLATE: Final[str] = 'device_roles_colortemplate.json'
COLOR_CSV: Final[str] = 'color.csv'
PATH_ROLE: Final[str] = os.path.join(
    os.path.dirname(os.getcwd()), DEVICE_ROLE)
PATH_COLOR: Final[str] = os.path.join(os.getcwd(), COLOR_TEMPLATE)
PATH_OUT: Final[str] = os.path.join(os.getcwd(), 'device_roles_colored.yaml')
PATH_DATA: Final[str] = os.path.join(
    os.path.dirname(os.getcwd()), 'datamodel_roles.md')


def set_role_color_by_csv_mark():
    """Create the device role yaml according to the markdown file.
    Use the csv file and in markdown colors indicated by '::<colorname>' 

    Input options:
        - set color by adding "::<colorname>" behind device role
          Note: if the color name is not a main color in csv, the color will be ignored
        - set color in csv file in column "choice" by <device_role>

    Color fill logic:
        - main roles get a different color each
        - children get the same darker tone of that color
        - the children of a child get the same darker tone 

    Warning: Errors are not neither logged or prevented by wrong input data
    """
    # get data color of csv
    df_cl = pd.read_csv(COLOR_CSV, delimiter=";",
                        dtype=defaultdict(lambda: str))
    df_cl.darker = df_cl.darker.str.split(",")
    df_cl[['color_name', 'choice']] = df_cl[[
        'color_name', 'choice']].apply(lambda col: col.str.lower())
    df_cl.color_name = df_cl.color_name.replace(r"\s", "-", regex=True)
    df_cl.loc[df_cl.choice.dropna().index, 'notes'] = "set by csv file"

    # get roles and possible color settings from markdown
    df_str = get_structure()
    df_str[['name', 'parent']] = df_str[[
        'name', 'parent']].apply(lambda col: col.str.lower())
    pre_mrk = pd.DataFrame(data=df_str.loc[df_str.name.str.contains(
        "::", na=False), 'name'].str.split("::", expand=True))
    try:
        pre_mrk.columns = ['role', 'color']
        # update df_cl list with markdown color settings
        for ind in pre_mrk.index:
            df_cl.choice[df_cl.color_name == pre_mrk.loc[ind]
                        ['color']] = pre_mrk.loc[ind]['role']
            df_cl.notes[df_cl.color_name == pre_mrk.loc[ind]
                        ['color']] = "markdown color"
    except ValueError:
        logger.info("No  color was set in markdown file.")
    df_str.name = df_str.name.replace(r"::.*", "", regex=True)
    df_str.parent = df_str.parent.replace(r"::.*", "", regex=True)


    # Create a dictionary to map color to choice
    color_to_choice = dict(zip(df_cl['choice'], df_cl['color']))
    color_to_choice.pop(np.nan, None)
    # set color from merged color table
    df_str['color'] = df_str['name'].map(
        lambda c: color_to_choice.get(c, np.nan))

    # update color list
    color_to_choice = list(df_cl.loc[df_cl.choice.isna(), 'color'])

    # set level 0
    df_str.loc[(df_str.level == 0) & (df_str.color.isna()), 'color'] = df_str.loc[(
        df_str.level == 0) & (df_str.color.isna())]['color'].map(lambda c: color_to_choice.pop(0))

    # update df_cl
    df_cl.choice = df_cl.color.map(
        lambda c: df_str.loc[df_str.color == c, 'name'].iloc[0])
    df_cl.notes = df_cl.notes.fillna("set in color function")

    # set level 1 ... n
    level = 1
    for level in range(1, df_str.level.max()+1):
        if level == 1:
            color_to_choice = dict(
                zip(df_cl['color'], df_cl['darker'].apply(lambda x: x[0])))
            df_str.loc[(df_str.level == level) & (df_str.color.isna()), 'color'] = df_str.loc[(df_str.level == level) & (
                df_str.color.isna())]['parent'].map(lambda c: color_to_choice.get(df_str.loc[df_str.name == c,
                                                                                             'color'].iloc[0], np.nan))
        else:
            color_to_choice = dict(zip(df_cl['darker'].apply(
                lambda x: x[level-2]), df_cl['darker'].apply(lambda x: x[level-1:])))
            for parent in df_str.loc[(df_str.level == level) & (df_str.color.isna())]['parent'].unique():
                df_str.loc[(df_str.level == level) & (df_str.color.isna())
                           & (df_str.parent == parent), 'color'] = color_to_choice.get(df_str.loc[df_str.name == parent, 'color'].iloc[0]).pop(0)
    # Export dataframe to yaml
    with open(PATH_OUT, 'w', encoding='utf-8') as file:
        yaml.dump(df_str.reset_index(drop=True).to_dict(
            orient='records'), file, sort_keys=False, indent=2)
    df_cl.to_csv('color_csv.log', sep=";", index=False)
    return True


def check_device_role_yaml():
    """check the device_role yaml against the markdown file."""
    with open(PATH_ROLE, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Convert the YAML data to a Pandas DataFrame
    df = pd.DataFrame.from_dict(data)

    if df.parent.isnull().sum():
        logger.warning(
            f"There are {df.parent.isnull().sum()} roles with no parent entry")
    else:
        logger.info("Every role has a parent entry")
    if len(df.drop_duplicates(subset=["slug"])) != len(df):
        logger.info("The file has duplicates according to slug.")
    df_slag = df.loc[df.slug.str.replace("-", " ") != df.name.str.lower()]
    if len(df_slag):
        logger.warning(
            "Slags and names are not following the naming convention")
        logger.warning(df_slag)
    else:
        logger.info("Slag and name are following the naming convention.")

    if df.vm_role.isnull().sum():
        logger.info(
            f"Missing vm_roles (num): {df.loc[df.vm_role.isnull().sum()]}")

    logger.info("Check if group roles are in json")
    df_struc = get_structure()
    if len(df_struc.loc[~df_struc.name.isin(df.slug)]):
        logger.info(
            "There are roles from markdown file missing in device_roles")
        logger.info(df_struc.loc[~df_struc.name.isin(df.slug)])
    if len(df.loc[~df.slug.isin(df_struc.name)]):
        logger.info(
            "There are roles in device_roles that are not in markdown overview:")
        logger.info(df.loc[~df.slug.isin(df_struc.name)])

    # check if parent counts are equal and with same name style
    count_dr = df.loc[df.parent != 'none',
                      'parent'].value_counts().sort_index()
    count_md = df_struc.loc[df_struc.parent !=
                            'none', 'parent'].value_counts().sort_index()

    if not (count_dr.index == count_md.index).all():
        logger.warning(
            "parent naming is different. Check out. Structure may be wrong.")
    else:
        if (count_dr == count_md).all():
            logger.info(
                "Number of children of each group devices is consistent between markdown and device role file.")
        else:
            logger.warning(
                'Number of children of each group devices is NOT consistent between markdown and device role file')
            logger.info(count_dr.loc[~(count_dr == count_md)])
            logger.info(count_md.loc[~(count_dr == count_md)])

    return


def set_color() -> bool:
    """Set color of device roles according to colortemplate.
    The group role determine the color. The offsprings have a 
    darker one.
    """
    with open(PATH_ROLE, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    with open(PATH_COLOR, 'r', encoding='utf-8') as f:
        device_roles_colorscheme = json.load(f)

    # Convert the YAML data to a Pandas DataFrame
    df = pd.DataFrame.from_dict(data)
    df_color = pd.DataFrame.from_dict(
        device_roles_colorscheme, orient='columns')

    # Set color for main device roles
    main_mask = df['parent'] == "none"
    try:
        df.loc[main_mask, 'color'] = df.loc[main_mask,
                                            'slug'].map(lambda x: df_color[x].color)
    except KeyError as e:
        logger.error(
            f'{e} is a main device role but not declared as one in color scheme.')

    # Set color for rest device roles
    df.loc[df.parent != "none",
           'color'] = df.loc[df.parent !=
                             "none", "slug"].map(lambda x: get_color(x, df, df_color))

    with open(PATH_OUT, 'w', encoding='utf-8') as file:
        yaml.dump(df.reset_index(drop=True).to_dict(
            orient='records'), file, sort_keys=False, indent=2)
    return True


def get_color(slug, df, df_color):
    """Returns color for offsprings of main devices."""
    parent = df.loc[df.slug == slug, 'parent'].iloc[0]
    # children of a "main" parent
    if parent in df_color.columns:
        logger.info(
            f'Set color {df_color.loc["children", parent]} for device role {slug} - child of main device role')
        return df_color.loc['children', parent]
    # it is a child of a "minor" parent group
    elif parent in df_color.index:
        logger.info(
            f'Set color {df_color.loc[parent].dropna().iloc[0]} for device role {slug} - child of a "minor" parent group')
        return df_color.loc[parent].dropna().iloc[0]
    else:
        # it is a children and has none
        logger.info(
            f'Set color {df_color.loc[slug, parent]} for device role{slug} - role has no children')
        return df_color.loc[slug, parent]


def get_structure():
    """Get Structure of markdown file. You need to copy and paste it here"""
    with open(PATH_DATA, 'r', encoding='utf-8') as f:
        raw_input = [line.replace('\n', '') for line in f.readlines()]
    # Prepare output structure
    parent = 'none'
    parent_tmp = 'none'
    df_rl = pd.DataFrame(columns=['name', 'parent', 'children', 'level'])
    df_rl = df_rl.astype({
        'name': str,
        'parent': str,
        'children': int,
        'level': int
    })
    df_prt = pd.DataFrame(columns=['lev_prt'], data=['none'])
    df_prt = df_prt.astype({
        'lev_prt': str
    })
    table = False
    level_last = 0
    for line in raw_input:
        if not table:
            if line.startswith('```markdown'):
                table = True
            continue
        elif table and line.startswith('```'):
            table = False
            continue
        elif table and line.startswith('Primary device role'):
            continue
        level = line.count('│')
        clean_line = re.sub(r'^[\s│├└─]*', '', line)
        clean_line = re.sub(r'[✅❗❓🚫]', '', clean_line).strip().lower()
        if not clean_line:  # Skip empty lines
            continue
        if level > level_last + 1:
            logger.error(
                f'Markdownfile für {clean_line} nicht korrekt, Sprung von level {level_last} auf {level}')
        df_prt = set_level_history(df_prt, parent_tmp, level, level_last)
        parent = df_prt.iloc[level]['lev_prt']
        new_rl = pd.DataFrame(
            [[clean_line, parent, 0, level]], columns=df_rl.columns)
        df_rl = pd.concat([df_rl, new_rl], ignore_index=True)
        parent_tmp = clean_line
        level_last = level

    counts = df_rl.loc[df_rl.parent != 'none', 'parent'].value_counts()
    df_rl.loc[df_rl['name'].isin(counts.index),
              'children'] = df_rl['name'].map(counts)
    # df_rl.name = df_rl.name.replace(r" ", r"-", regex=True)
    # df_rl.parent = df_rl.parent.replace(r" ", r"-", regex=True)
    df_rl[['name', 'parent']] = df_rl[['name', 'parent']].apply(
        lambda col: col.replace(" ", "-", regex=True))

    return df_rl


def set_level_history(df_prt, parent_tmp, level, level_last):
    """Take care of collecting the parent hierarchy."""
    if level == 0:
        # delete parent history
        df_prt = df_prt.iloc[:1]
    else:
        if level > level_last:
            df_prt.loc[len(df_prt)] = [parent_tmp]
        elif level < level_last:
            df_prt = df_prt.iloc[:(level+1)]
    return df_prt


if __name__ == "__main__":
    print('READY TO USE.')
