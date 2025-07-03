# Data Model in NetBox

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](Discussion_datamodel.md)

---

This show how the data model is placed and the status of implementation.

## Fragen/TODO

Open questions:

- [NetBox model](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/)

## TODOS

- a links to the fields and use # sign check
- sortieren nach device, device type und software
- update device type issue
- check hardware as core field?
- check communication partner value

### Legend

```markdown
    * ❓ = The attribution is unclear
    * ❗ = There is a conflict about this attribute which is addressed by the link. Adjustments are mandatory.
    * ℹ️ = There is information about this attribute which is addressed by the link
    * 🔨 = Adjustments to the current state of the DDDC plugin are necessary
```

*Table 2: Data Model for NetBox Plugins by DINA Community.*

|Name   | NetBox | Field | Action |Description/Purpose |
| - | - | - | - |- |
| **Device** |  |  |  | |
|Article Number         | DeviceType:part_number | custom | see [part number](datamodel_attributes.md#part-number)  --> delete 🔨  | -|
| Device Name | device:name | core | - |Potentially useful for understanding context and function of the device in the network if included in host naming conventions |
| Device Role (primary)  | [DeviceRole:name](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/devicerole#name) | core| 🔨 role yaml has to be adjusted | useful for understanding context and function of the device in the network |
|Device Role (secondary)| DeviceRole:name_minor    | custom| -| multiple objects field |
|Serial number       | [Device: serial](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/device/#serial-number)             | core | specific serial number of device | here weitermache 🔨 🔨 🔨 🔨 🔨 |
|Safety                 | Device:safety            | custom | device is used for safety functionality. Information also in CVSS available. |-|
|[Exposure](datamodel_attributes.md#exposure) | Device:exposure | custom | exposure to other network zones |-|
|Date of Manufacture    | Device:year              | :hammer: new :hammer: | Year of construction of the device. Useful in determining obsolescence and possible shifts in ownership of device type. | -|
|Inventory Number | Device:Inventory_number | :hammer: new :hammer: |  Not relevant for vulnerability matching. However, for linking the dataset to other internal products like SAP | - |
| **Device Type** |  |  |  | |
|Manufacturer           | Manufacturer:name        | core| manufacturer **of device type** like  ABB, Schneider Electric| - |
|Device Type Name       | manufacturer + model     | discarded | used for assign a device to a device type.| [Details](datamodel_attributes.md#part-number#device-family) |
|Device Family          | [DeviceType:device_family]((https://netboxlabs.com/docs/netbox/en/stable/models/dcim/devicetype/)) | custom /❗[Device Type](#discussion-device-type) | usually family a model is assigned to | -|
|[Model Number](datamodel_attributes.md#model)         | DeviceType:model  | core/❗[Device Type](#discussion-device-type) | Model number given by the manufacturer. One specification of a device_family like 6RA8096-4MV62-0AA0| - |
|[SKU](datamodel_attributes.md#part-number)                  | DeviceType:part_number   | core/❗[Device Type](#discussion-device-type) | SKU (stock keeping unit) also known as part number | - |
|Device Description     | DeviceType:device_description | custom/❗[Device Type](#discussion-device-type) | additional, optional field for detailed device description| [Device Description](#device-description)|
|Hardware Name           |DeviceType:hardware_name  | custom/❗[Device Type](#discussion-device-type)  |HW  of device, not of installed software (flag must be set in NetBox) | -|
|Hardware version        |DeviceType:hardware_version | custom/❗[Device Type](#discussion-device-type) | Hardware version of the product; use "N/A" if just one version was build; use "unknown" if not known. The notations of the manufacturer should not be altered. | see Software version |
| **Software** |  |  |  ||
|Software Manufacturer    |Software:manufacturer | :hammer: new :hammer: | distinguish between manufacturer of the device | |
|Firmware Name           |Software:name       | custom  |FW of device, not of installed software (flag must be set in NetBox) | -|
|Firmware Version        |Software:version    | :hammer: modify :hammer:  | FW version of device, not of installed software (flag must be set in NetBox). | see Software version |
|Communication partner - IP| Communication:dst_ip_addr | core | not observed CP but expected one (source of truth) for IDS | - |
|Communication partner - Protocol| Communication:transport_protocol| core | not observed CP but expected one (source of truth) |-|
|Software Name           |Software:name       | custom   |The name this particular version is given| - |
|Software Version        |[Software:version](datamodel_attributes.md#part-number#version-number)    | :hammer: modify :hammer: | :information_source: There are plenty of valid notations for version schema such as MAYOR.MINOR.PATCH.BUILD or YEAR-MONTH-DATE or hash value. Therefore, there is no common standard. | - |
|[CPE](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31331-full-product-name-type---product-identification-helper---cpe)                   |DeviceType:cpe     | custom | Common Platform Enumeration (CPE), is also used as CSAF product identification helper| -|
|[Hashes](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31332-full-product-name-type---product-identification-helper---hashes)                  |Software:Hashes    | custom | for firmware and applications software, is also used as CSAF product identification helper |-|
|[PURL](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31334-full-product-name-type---product-identification-helper---purl)                   |Software:Hashes    | custom | package URL (purl), is also used as CSAF product identification helper | - |
|[SBOM_urls](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31335-full-product-name-type---product-identification-helper---sbom-urls)             |Software:sbom_urls | custom | The URL is a unique identifier. The content is secondary| - |
|[x_generic_uris](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31338-full-product-name-type---product-identification-helper---generic-uris)          |Software:x_generic_uris AND DeviceType:x_generic_uris| custom |unique id given by the vendor (e.g. [#649](https://github.com/oasis-tcs/csaf/issues/649))| - |

### Tasks

- adjust role yaml files (Malcolm PR)

#### Code

##### device_update.py

device_update.py#
def 
deprecated because roles can have child/parents

device_update.py#L288-302
def 

|File|function|Lines|Action|Comment|Issue|
|-|-|-|-|-|-|
|device_update.py| change_device_router |L288-302 | deprecated  |deprecated because roles can have child/parents  | #1 |
|device_update.py| change_device_role   |L161-178 | revision    |Need revision for handling child parents properly| #1 |
|device_update.py| change_device_type_keep_manufacturer| L119-138| revision| check if handled properly | branch P625|

