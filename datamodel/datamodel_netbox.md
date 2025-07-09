# Data Model in NetBox

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](Discussion_datamodel.md)

---

description

- FW of device, not of installed software (flag must be set in NetBox)


This show how the data model is placed and the status of implementation.

## Legend

```markdown
    * ❓ = The attribution is unclear
    * ❗ = There is a conflict about this attribute which is addressed by the link. Adjustments are mandatory.
    * ℹ️ = There is information about this attribute which is addressed by the link
    * 🔨 = Adjustments to the current state of the DDDC plugin are necessary
```

## Table 2: Data Model for NetBox Plugins by DINA Community

|Name   | NetBox | Field | Action |Description/Purpose |
| - | - | - | - |- |
| **Device** |  |  |  | |
|Article Number         | DeviceType:part_number | custom |  delete   | -|
| [Device Name](datamodel_attributes.md#device-name) | [Device:name](https://netboxlabs.com/docs/netbox/models/dcim/device/#name) | core | - |Potentially useful for understanding context and function of the device in the network if included in host naming conventions |
| [Device Role (primary)](datamodel_attributes.md#role-primary)  | [DeviceRole:name](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/devicerole#name) | core| [role.yml](https://github.com/DINA-community/String-Sysiphos/blob/data_model/datamodel/device_roles.yml)| useful for understanding context and function of the device in the network |
|[Device Role (secondary)](datamodel_attributes.md#role-secondary)| DeviceRole:name_minor    | custom| -| multiple objects field |
|[Serial number](datamodel_attributes.md#serial-number)       | [Device: serial](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/device/#serial-number)             | core |- | specific serial number of device |
|[Safety](datamodel_attributes.md#safety)                 | Device:safety            | custom |- | device is used for safety functionality. Information also in CVSS available. |
|[Exposure](datamodel_attributes.md#exposure) | Device:exposure | custom | - |exposure to other network zones |
|[Date of Manufacture](datamodel_attributes.md#date-of-manufacture)    | Device:year              | new |:hammer: | Year of construction of the device. Useful in determining obsolescence and possible shifts in ownership of device type. |
|[Inventory Number](datamodel_attributes.md#device-key)  | Device:Inventory_number | new | :hammer: |  Not relevant for vulnerability matching. However, for linking the dataset to other internal products like SAP |
| **Device Type** |  |  |  | |
|[Manufacturer](datamodel_attributes.md##manufacturer-of-device-type)  | [Manufacturer:name](https://netboxlabs.com/docs/netbox/models/dcim/manufacturer/)        | core| -| manufacturer **of device type** like  ABB, Schneider Electric|
|Device Type Name       | manufacturer + model     | core | generated [#14125](https://github.com/netbox-community/netbox/discussions/14125) | used for assign a device to a device type. [Details](datamodel_attributes.md#part-number#device-family) |
|[Device Family](datamodel_attributes.md#device-family)          | [DeviceType:device_family]((https://netboxlabs.com/docs/netbox/en/stable/models/dcim/devicetype/)) | custom | - |usually family a model is assigned to |
|[Model Number](datamodel_attributes.md#model)         | DeviceType:model  | core | - |Model number given by the manufacturer. One specification of a device_family like 6RA8096-4MV62-0AA0|
|[SKU](datamodel_attributes.md#part-number)                  | DeviceType:part_number   | core |-| SKU (stock keeping unit) also known as part number |
|Device Description     | DeviceType:device_description | now core | adapt DDDC-plugin |additional, optional field for detailed device description. Also it can be used for CSAF matchting as full produce name|
|[Hardware Name](datamodel_attributes.md#hardware-name)           |DeviceType:hardware_name  | custom |-| HW  of device, not of installed software (flag must be set in NetBox) |
|[Hardware version](datamodel_attributes.md#hardware-version)        |DeviceType:hardware_version | custom|-| Hardware version of the product; use "N/A" if just one version was build; use "unknown" if not known. The notations of the manufacturer should not be altered. | see Software version |
| **Software** |  |  |  ||
|[Software Manufacturer](datamodel_attributes.md#software-manufacturer)    |Software:manufacturer | new | :hammer: | distinguish between manufacturer of the device |
|[Firmware Name](datamodel_attributes.md#software-name) |Software:name  | custom  |-|FW of device, not of installed software (flag must be set in NetBox) | -|
|[Firmware Version](datamodel_attributes.md#software-version)   |Software:version    |  modify |:hammer:  | FW version of device, not of installed software (flag must be set in NetBox). |
|[Communication partner - IP](datamodel_attributes.md#communication-partner---ip)| Communication:dst_ip_addr | core | -|not observed CP but expected one (source of truth) for IDS | - |
|[Communication partner - Protocol](datamodel_attributes.md#protocolservices)| Communication:transport_protocol| core | -|not observed CP but expected one (source of truth) |-|
|[Software Name](datamodel_attributes.md#software-name)           |Software:name       | custom   |-|The name this particular version is given| - |
|[Software Version](datamodel_attributes.md#software-version)        |Software:version    | modify | :hammer: | :information_source: There are plenty of valid notations for version schema such as MAYOR.MINOR.PATCH.BUILD or YEAR-MONTH-DATE or hash value. Therefore, there is no common standard. |
|[CPE](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31331-full-product-name-type---product-identification-helper---cpe)                   |DeviceType:cpe      | custom |- | Common Platform Enumeration (CPE), is also used as CSAF product identification helper|
|[Hashes](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31332-full-product-name-type---product-identification-helper---hashes)                  |Software:Hashes   | custom |- | for firmware and applications software, is also used as CSAF product identification helper |
|[PURL](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31334-full-product-name-type---product-identification-helper---purl)                   |Software:Hashes    | custom |- | package URL (purl), is also used as CSAF product identification helper | 
|[SBOM_urls](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31335-full-product-name-type---product-identification-helper---sbom-urls)             |Software:sbom_urls | custom |- | The URL is a unique identifier. The content is secondary| - |
|[x_generic_uris](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31338-full-product-name-type---product-identification-helper---generic-uris)          |Software:x_generic_uris AND DeviceType:x_generic_uris| custom |- | unique id given by the vendor (e.g. [#649](https://github.com/oasis-tcs/csaf/issues/649))| - |
