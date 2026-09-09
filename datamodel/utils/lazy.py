"""
This script checks the device schema in the parent folder.
In addition, the color of each device can be specified using
the color template.
Note that devices assigned to a parent device have the same color,
which is usually darker than the color of the parent device.

Functions

set_role_color_by_csv_mark --> set color by csv file
check_device_role_yaml -> check if device_role and markdown are equal
set color --> set color by COLOR_TEMPLATE json file
get color --> internal function
get structure --> gets structure from markdown file
set level history --> internal function

"""

import json
import re
from pathlib import Path
from typing import Final
import argparse
import yaml
import pandas as pd
from loguru import logger


DEVICE_ROLE: Final[Path] = Path.cwd().parent / "device_roles.yml"
COLOR_TEMPLATE: Final[Path] = Path.cwd() / "device_roles_colortemplate.json"
COLOR_CSV: Final[Path] = Path.cwd() / "color.csv"
PATH_OUT: Final[Path] = Path.cwd() / "device_roles_colored.yaml"
PATH_DATA: Final[Path] = Path.cwd().parent / "datamodel_roles.md"

logger.remove()
logger.add("lazy.log", format="{level}-{message}", mode="w")


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
    validate_paths()
    # get data color of csv
    df_cl = pd.read_csv(
        COLOR_CSV, delimiter=";",
        dtype=str,
        on_bad_lines="skip"
    )
    df_cl["darker"] = df_cl["darker"].fillna("").str.split(",")
    df_cl[["color_name", "choice"]] = df_cl[["color_name",
                                             "choice"]].apply(
                                                 lambda col: col.str.lower())
    df_cl["color_name"] = df_cl["color_name"].str.replace(r"\s", "-", regex=True)

    # Apply markdown-sourced color overrides safely
    mask_notes = df_cl["choice"].notna()
    df_cl.loc[mask_notes, "notes"] = "set by csv file"

    # get roles and possible color settings from markdown
    df_str = get_structure()
    df_str["name"] = df_str["name"].str.strip().str.lower()
    df_str["parent"] = df_str["parent"].str.strip().str.lower()
    color_mask = df_str["name"].str.contains("::", na=False)
    if color_mask.any():
        pre_mrk = df_str.loc[color_mask, "name"].str.split("::", expand=True)
        try:
            pre_mrk.columns = ["role", "color"]
            for _, row in pre_mrk.iterrows():
                target_color = row["color"]
                df_cl.loc[df_cl["color_name"] == target_color, "choice"] = row["role"]
                df_cl.loc[df_cl["color_name"] == target_color, "notes"] = "markdown color"
        except ValueError as e:
            logger.warning(f"Failed to apply markdown color overrides: {e}")

    df_str["name"] = df_str["name"].replace(r"::.*", "", regex=True)
    df_str["parent"] = df_str["parent"].replace(r"::.*", "", regex=True)

    # Create a dictionary to map color to choice
    color_to_choice = dict(zip(df_cl["choice"].dropna(), df_cl["color"].dropna()))

    # set color from merged color table
    df_str["color"] = df_str["name"].map(color_to_choice)

    # Assign fallback colors to level 0 if missing
    fallback_colors = df_cl.loc[df_cl["choice"].isna(), "color"].tolist()
    mask_level0 = (df_str["level"] == 0) & (df_str["color"].isna())
    if fallback_colors:
        df_str.loc[mask_level0, "color"] = [fallback_colors.pop(0) for _ in range(mask_level0.sum())]

    # update color list
    color_to_choice = list(df_cl.loc[df_cl.choice.isna(), "color"])

    # set level 1 ... n
    for level in range(1, df_str.level.max() + 1):
        mask_level = (df_str["level"] == level) & (df_str["color"].isna())
        if not mask_level.any():
            continue
        if level == 1:
            darker_map = dict(zip(df_cl["color"], df_cl["darker"].apply(lambda x: x[0] if x else None)))
            df_str.loc[mask_level, "color"] = df_str.loc[mask_level, "parent"].map(
                lambda p: darker_map.get(df_str.loc[df_str["name"] == p, "color"].iloc[0]) if p in df_str["name"].values else None
            )
        else:
            darker_map = dict(zip(
                df_cl["darker"].apply(lambda x: x[level-2] if len(x) > level-2 else None),
                df_cl["darker"].apply(lambda x: x[level-1:] if len(x) > level-1 else None)
            ))
            for parent in df_str.loc[mask_level, "parent"].unique():
                parent_color = df_str.loc[df_str["name"] == parent, "color"].values[0]
                if pd.notna(parent_color) and parent_color in darker_map:
                    shade_stack = darker_map[parent_color]
                    df_str.loc[(df_str["level"] == level) &
                               (df_str["parent"] == parent) &
                               (df_str["color"].isna()),
                               "color"] = shade_stack.pop(0)

    with open(DEVICE_ROLE, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Overwrite device_roles with csv setting
    df = pd.DataFrame.from_dict(data)
    df['color'] = df['slug'].map(df_str.set_index('name')['color']).fillna(df['color'])
    df["description"] = df["description"].fillna("missing")
    # Export dataframe to yaml
    PATH_OUT_CSV = PATH_OUT.with_name(f"{PATH_OUT.stem}_csv{PATH_OUT.suffix}")

    with open(PATH_OUT_CSV, "w", encoding="utf-8") as file:
        yaml.dump(
            df.reset_index(drop=True).to_dict(orient="records"),
            file,
            sort_keys=False,
            indent=2,
        )
    df_cl.to_csv("color_csv-log.csv", sep=";", index=False)
    logger.success(f"Generated {PATH_OUT_CSV.name}")
    return


def check_device_role_yaml():
    """Check the device_role yaml against the markdown file."""
    with open(DEVICE_ROLE, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Convert the YAML data to a Pandas DataFrame
    df = pd.DataFrame.from_dict(data)

    if df.parent.isnull().sum():
        logger.warning(
            f"There are {df.parent.isnull().sum()} roles with no parent entry"
        )
    else:
        logger.success("Every role has a parent entry")
    if len(df.drop_duplicates(subset=["slug"])) != len(df):
        logger.info("The file has duplicates according to slug.")
    df_slag = df.loc[df.slug.str.replace("-", " ") != df.name.str.lower()]
    if len(df_slag):
        logger.warning(
            "Slags and names are not following the naming convention"
        )
        logger.warning(df_slag)
    else:
        logger.success("Slag and name are following the naming convention.")

    if df.vm_role.isnull().sum():
        logger.info(
            f"Missing vm_roles (num): {df.loc[df.vm_role.isnull().sum()]}"
        )

    df_struc = get_structure()
    # delete given color settings
    df_struc["name"] = df_struc.name.replace(r"::.*", "", regex=True)
    df_struc["parent"] = df_struc.parent.replace(r"::.*", "", regex=True)
    if len(df_struc.loc[~df_struc.name.isin(df.slug)]):
        logger.info(
            "There are roles from markdown file missing in device_roles"
        )
        logger.info(df_struc.loc[~df_struc.name.isin(df.slug)])
    if len(df.loc[~df.slug.isin(df_struc.name)]):
        logger.info(
            "There are roles in device_roles that are not in markdown overview:"
        )
        logger.info(df.loc[~df.slug.isin(df_struc.name)])

    # check if parent counts are equal and with same name style
    count_dr = df.loc[df.parent != "none", "parent"].value_counts().sort_index()
    count_md = (
        df_struc.loc[df_struc.parent != "none", "parent"]
        .value_counts()
        .sort_index()
    )

    if not (count_dr.index == count_md.index).all():
        logger.warning(
            "parent naming is different. Check out. Structure may be wrong."
        )
    else:
        if (count_dr == count_md).all():
            logger.success(
                "Number of children of each group devices \
                is consistent between markdown and device role file."
            )
        else:
            logger.warning(
                "Number of children of each group devices is NOT \
                    consistent between markdown and device role file"
            )
            logger.info(count_dr.loc[~(count_dr == count_md)])
            logger.info(count_md.loc[~(count_dr == count_md)])


def set_color() -> bool:
    """Set color of device roles according to colortemplate.json
    The group role determine the color. The offsprings are
    darker.
    """
    with open(DEVICE_ROLE, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    with open(COLOR_TEMPLATE, "r", encoding="utf-8") as f:
        device_roles_colorscheme = json.load(f)

    # Convert the YAML data to a Pandas DataFrame
    df = pd.DataFrame.from_dict(data)
    df_color = pd.DataFrame.from_dict(
        device_roles_colorscheme, orient="columns"
    )

    # Set color for main device roles
    main_mask = df["parent"] == "none"
    try:
        df.loc[main_mask, "color"] = df.loc[main_mask, "slug"].map(
            lambda x: df_color[x].color
        )
    except KeyError as e:
        logger.error(
            f"{e} is a main device role but not declared as one in color scheme."
        )

    # Set color for rest device roles
    df.loc[df.parent != "none", "color"] = df.loc[
        df.parent != "none", "slug"
    ].map(lambda x: get_color(x, df, df_color))
    df["description"] = df["description"].fillna("missing")
    PATH_OUT_JSON = PATH_OUT.with_name(f"{PATH_OUT.stem}_json{PATH_OUT.suffix}")
    with open(PATH_OUT_JSON, "w", encoding="utf-8") as file:
        yaml.dump(
            df.reset_index(drop=True).to_dict(orient="records"),
            file,
            sort_keys=False,
            indent=2,
        )
    logger.success(f"Generated {PATH_OUT_JSON.name}")
    return


def get_color(slug, df, df_color):
    """Returns color for offsprings of main devices."""
    parent = df.loc[df.slug == slug, "parent"].iloc[0]
    # children of a "main" parent
    if parent in df_color.columns:
        logger.info(
            f"Set color {df_color.loc['children', parent]} for device role {slug} - child of main device role"
        )
        return df_color.loc["children", parent]
    # it is a child of a "minor" parent group
    elif parent in df_color.index:
        logger.info(
            f"Set color {df_color.loc[parent].dropna().iloc[0]} for device role {slug} - child of a 'minor' parent group"
        )
        return df_color.loc[parent].dropna().iloc[0]
    else:
        # it is a children and has none
        logger.info(
            f"Set color {df_color.loc[slug, parent]} for device role{slug} - role has no children"
        )
        return df_color.loc[slug, parent]


def get_structure():
    """Get Structure of markdown file. You need to adjust the structure
    in PATH_DATA."""
    with open(PATH_DATA, "r", encoding="utf-8") as f:
        raw_input = [line.replace("\n", "").replace("\r", "") for line in f]

    parent = "none"
    parent_tmp = "none"
    df_rl = pd.DataFrame(columns=["name", "parent", "children", "level"])
    df_rl = df_rl.astype({"name": str,
                          "parent": str,
                          "children": int,
                          "level": int})
    df_prt = pd.DataFrame(columns=["lev_prt"], data=["none"])
    df_prt = df_prt.astype({"lev_prt": str})
    level_last = 0
    table_mode = False

    for line in raw_input:
        # State machine for markdown table boundaries
        if not table_mode:
            if line.startswith("```markdown"):
                table_mode = True
            continue
        if table_mode and line.startswith("```"):
            table_mode = False
            continue
        if table_mode and "Primary device role" in line:
            continue

        # Calculate indentation level
        level = line.count("│")

        # Strip tree characters and whitespace safely
        clean_line = re.sub(r"^[\s│├└─\u2502\u251c\u2514\u2500]*", "", line)
        clean_line = re.sub(r"[✅❗❓🚫]", "", clean_line).strip().lower()

        if not clean_line:
            continue

        # Guard against malformed hierarchy jumps
        if level > level_last + 1:
            logger.error(f"Markdown hierarchy error for '{clean_line}': Jump from level {level_last} to {level}")
            level_last = level
            continue
        df_prt = set_level_history(df_prt, parent_tmp, level, level_last)
        parent = df_prt.iloc[level]["lev_prt"]
        new_rl = pd.DataFrame([[clean_line, parent, 0, level]],
                              columns=df_rl.columns)
        df_rl = pd.concat([df_rl, new_rl], ignore_index=True)
        parent_tmp = clean_line
        level_last = level

    # Calculate children counts safely
    counts = df_rl.loc[df_rl["parent"] != "none", "parent"].value_counts()
    df_rl.loc[df_rl["name"].isin(counts.index), "children"] = df_rl["name"].map(counts)

    # Normalize spacing to hyphens for slug consistency
    df_rl[["name", "parent"]] = df_rl[["name", "parent"]].apply(lambda col: col.str.replace(" ", "-", regex=True))
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
            df_prt = df_prt.iloc[: (level + 1)]
    return df_prt


def validate_paths() -> None:
    """Ensure all required configuration files exist before processing."""
    for p in [DEVICE_ROLE, COLOR_TEMPLATE, COLOR_CSV, PATH_DATA]:
        if not p.exists():
            logger.error(f"Required path not found: {p}")
            raise FileNotFoundError(f"Missing configuration file: {p}")
    logger.info("All configuration paths validated successfully.")


def main():
    parser = argparse.ArgumentParser(
        prog="lazy.py",
        description="Run setup with the selected configuration.",
        epilog="Note that the file names are fixed",
    )

    parser.add_argument(
        "command",
        nargs="?",
        choices=["csv", "json"],
        default=None,
        help="Command to run: csv or json. If omitted, perform format check.",
    )

    args = parser.parse_args()

    if args.command is None:
        # Default setup
        print("Running default setup")
        check_device_role_yaml()
    elif args.command == "json":
        print("Running set color by json input")
        check_device_role_yaml()
        set_color()
    elif args.command == "csv":
        check_device_role_yaml()
        print("Running set color by csv input")
        set_role_color_by_csv_mark()


if __name__ == "__main__":
    main()
