# String-Sysiphos

> This repository provides regular expressions and dictionaries for the repository [`String-Atlas`](https://github.com/DINA-community/String-Atlas).

String-Sysiphos is a collection of Word-books and regular expression, focusing on String consistency, normalization and mapping for CSAF and OT-Network Assets. This collection was designed for the [`DINA-community`](https://github.com/DINA-community) project, surrounding [`Malcolm`](https://github.com/cisagov/Malcolm) and [`DDDC`](https://github.com/DINA-community/DDDC-Netbox-plugin).

Note that the attributes the regular expressions are pointing to are those used for the NetBox plugins.

## Dictionaries

### Synonyms

The synonyms are case insensitive and have the purpose to normalize the input.

### Normalization

Pattern for cleaning.

### Regular expressions

Regular expressions for mining information out of a text (short or long string)

### Device_list

Dictionary for several attributes, especially device ones.

## NetBox libraries

This libraries are a result of the String-Atlas or student thesis as a byproduct.

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

> Note that this file is located only in the branch `data_model` at the moment.

`device_roles.yml` provided role reflecting the hierarchical feature for device roles since NetBox version [`4.3`](https://netboxlabs.com/docs/netbox/release-notes/version-4.3#hierarchical-device-roles-18245).

```yaml
- name: physical-sensor
  slug: physical-sensor
  parent: fielddevice
```

## License

The software was developed on behalf of the [BSI](https://www.bsi.bund.de) \(Federal Office for Information Security\)

Copyright &copy; 2024-2025 by DINA-Community Apache 2.0 License. [See License](/LICENSE)
