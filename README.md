# String-Sysiphos

String-Sysiphos is a collection of word-books and regular expression, focusing on string consistency, normalization and mapping for CSAF and OT-Network Assets. This collection was designed for the [`DINA-community`](https://github.com/DINA-community) project, surrounding [`Malcolm`](https://github.com/cisagov/Malcolm) and [`DDDC`](https://github.com/DINA-community/DDDC-Netbox-plugin).

Note that the attributes the regular expressions are pointing to are those used for the NetBox plugins.

## Dictionaries String-Atlas

| File                  | Description                                                                           |
| --------              | --------                                                                              |
| config.json           | Columns for data frame to process csaf documents                                      |
| normalisation.yaml    | Pattern for cleaning.                                                                 |
| re_data.yaml          | Regular expressions for mining information out of a text (short or long string)       |
| synonym.yaml          | The synonyms are case insensitive and have the purpose to normalize the input.        |

## Data model

Fundamental to any approach to securing and protecting OT systems is the complete and accurate identification of all OT assets and systems and how they connect and communicate across an organization’s networks.  
This data should be standardized. Under [datamodel](/datamodel/datamodel.md) the data models with its attributes and roles are explained. Furthermore, the mapping for the [DDDC-Plugin](https://github.com/DINA-community/DDDC-Netbox-plugin) for [NetBox](https://netboxlabs.com/docs/netbox/en/stable/) with [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html) is illustrated.

## NetBox Files

### Manufacturers

Within the `manufacturers.yaml` manufactures are listed which were extracted from CSAF documents mainly and enriched with info and slug field.
The field `group` divided the companies into different working areas:

- Group1: Core industrial hardware/components (e.g. B&R, Beckhoff).
- Group2: Industrial hardware with slight uncertainty or overlap to other group, also default input of Malcolm
- Group3: IT-hardware products (networking, surveillance, radio).
- Group4: Safety related but not directly in industrial environment (locks, alarm, webcam, acoustic)
- Group5: Medical hardware
- Group6: Pure software or CAD/engineering tools.
- Group7: Group for remaining companies

### Device Roles

`device_roles.yml` provided role reflecting the hierarchical feature for device roles since [NetBox 4.3](https://netboxlabs.com/docs/netbox/release-notes/version-4.3#hierarchical-device-roles-18245).

```yaml
- name: physical-sensor
  slug: physical-sensor
  parent: fielddevice
```

## License

The software was developed on behalf of the [BSI](https://www.bsi.bund.de) \(Federal Office for Information Security\)

Copyright &copy; 2024-2026 by DINA-Community Apache 2.0 License. [See License](/LICENSE)
