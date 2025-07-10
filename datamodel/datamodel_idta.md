# Data model within NetBox

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](datamodel_idta.md)

---

## Data Model for OT environment

With the [asset administration shell](https://webstore.iec.ch/publication/65628), there will be plenty of information about a device. However, which of those should be used for mapping vulnerabilities to a device? In the following table three documents of the IDTA are used to identify attributes for vulnerability mapping with CSAF and where this attributes can or should be find in Netbox.

> The NetBox column shows where the attribute would be found if it were implemented in NetBox. The status of implementation can be found under [Data model Mapping NetBox](datamodel_netbox.md). Correspondingly for CSAF see [Data model Mapping CSAF](datamodel_csaf.md)

*Table 1: Information for describing a device for vulnerability matching.*

| AAS | NetBox | CSAF | Description from AAS (mostly) | Relevant for CSAF matching                     | Source |
|  -           |  - | -  |- | - | - |
| Manufacturer Name| [Manufacturer:Name](datamodel_attributes.md#manufacturer-of-device-type) | vendor | Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market |Yes | [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Part number| [DeviceType:part_number](datamodel_attributes.md#part-number) | sku |unique product identifier of the manufacturer, also called [article number](#idta-02006-2-0) in IDTA| Yes |  [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Order Code| DeviceType:order_code | N/A | By manufactures issued unique combination of numbers and letters used to identify the device for ordering. | No | [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Product Designation | :question: device:comments | optional [/document/notes_t/ (line 340-400)](https://github.com/oasis-tcs/csaf/blob/master/csaf_2.0/json_schema/csaf_json_schema.json) | short description of the product, product group or function | No | [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Product Root| :question: deviceType:Role | N/A | Top level of a 3 level manufacturer specific product hierarchy (e. g. flow meter) | No | [IDTA 02006-2-0](#idta-02006-2-0)  |
| Manufacturer Product Family | [DeviceType:family](datamodel_attributes.md#device-family) | product_family |2nd level of a 3 level manufacturer specific product hierarchy | yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| Manufacturer Product Type | [DeviceType:model](datamodel_attributes.md#model)| product_name | Characteristic to differentiate between different products of a product family or special variants. :information_source: One of the two properties Manufacturer `Product Family` or Manufacturer `Product Type`  must be provided according to EU Machine Directive 2006/42/EC.| Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| *unknown* | [DeviceType:Description](datamodel_attributes.md#device-type-description) | x_generic_uris | :information_source: own additional level to a 3 level manufacturer specific product hierarchy| Yes | *unknown* |
| serial number| [Device:serial_number](datamodel_attributes.md#serial-number) | serial_number |unique combination of numbers and letters used to identify the device once it has been manufactured | Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| Date of Manufacture| [Device:year](datamodel_attributes.md#date-of-manufacture)| N/A| Date from which the production and / or development process is completed or from which a service is provided completely |No | [IDTA 02006-2-0](#idta-02006-2-0) |
| HardwareVersion| [DeviceType:hardware_version](datamodel_attributes.md#hardware-version)| product_version and product_version_range| :information_source: [Version](datamodel_attributes.md#hardware-version)  of the hardware supplied with the device|Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| FirmwareVersion| [Software:version](datamodel_attributes.md#software-version) + flag "is firmware"| product_version and product_version_range| :information_source: [Version](datamodel_attributes.md#software-version) of the firmware supplied with the device|Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| SoftwareVersion| [Software:version](datamodel_attributes.md#software-version)| product_version and product_version_range| :information_source: [Version](datamodel_attributes.md#software-version) of the software used by the device |Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| URI | [x_generic_uris](datamodel_attributes.md#x_generic_uris) | x_generic_uris |Unique global identification of the product using a universal resource identifier (URI)| Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| SoftwareType | [SoftwareType](datamodel_attributes.md#software-type) | N/A |The type of the software (category, e.g. Runtime, Application, Firmware, Driver, etc.) | Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| Version Name| [Software:version_name](datamodel_attributes.md#software-name) | x_generic_uris |The name this particular version is given (e. g. focal fossa) | Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| Version Info| Version Info | N/A | Provides a textual description of most relevant characteristics of the version of the software | No | [IDTA 02007-1-0](#idta-02007-1-0) |
| Manufacturer Name | [Manufacturer Name](datamodel_attributes.md#software-manufacturer)  | vendor in product_tree for this specific product| Creator of the software | Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| *unknown* | :question:Device:asset_tag / Device:Inventory or Software:x_generic_uris | x_generic_uris | Link to other company intern products like SAP | Yes | *unknown*|

### Literature

#### IDTA 02003-1-2

- **Title**: Generic Frame for Technical Data for Industrial Equipment in Manufacturing.
- **Section**: SMC GeneralInformation
- **Publisher**: Industrial digital twin Association
- **Year**: 2022
- **Source**: [IDTA Homepage](https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02003-1-2_Submodel_TechnicalData.pdf)

#### IDTA 02006-2-0

- **Title**: Digital Nameplate for Industrial Equipment
- **Section**: Nameplate
- **Publisher**: Industrial digital twin Association
- **Year**: 2022
- **Source**: [IDTA Homepage](https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02006-2-0_Submodel_Digital-Nameplate.pdf)

#### IDTA 02007-1-0

- **Title**: Nameplate for Software in Manufacturing
- **Section**: SoftwareNameplateType
- **Publisher**: Industrial digital twin Association
- **Year**: 2023
- **Source**: [IDTA Homepage](https://industrialdigitaltwin.org/wp-content/uploads/2023/08/IDTA-02007-1-0_Submodel_Software-Nameplate.pdf)
