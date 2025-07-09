# Data model within NetBox

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](datamodel_idta.md)

---

> Note that this page reflects former work that leads to the single files for NetBox CSAF and attributes. It is still included to show mapping with IDTA  
>❗ File will be adjusted to be up to date

Using Netbox in industrial control systems (ICS), the [Data Model of Netbox](https://netboxlabs.com/docs/netbox/en/stable/) has to be modified by custom fields and plugins. Still, there are some major adjustments to be made for the device type in order to use it for matching the asset data base with the Common Security Advisory Framework [CSAF](https://csaf.io).

## Datamodel for OT environment

With the [asset administration shell](https://webstore.iec.ch/publication/65628), there will be plenty of information about a device. However, which of those should be used for mapping vulnerabilities to a device? In the following table three documents of the IDTA are used to identify attributes for vulnerability mapping with CSAF and where this attributes can or should be find in Netbox.

### Legend

```markdown
    * ❓ = The attribution is unclear
    * ❗ = There is a conflict about this attribute which is addressed by the link. Adjustments are mandatory.
    * ℹ️ = There is information about this attribute which is addressed by the link
    * 🔨 = Adjustments to the current state of the DDDC plugin are going to be performed by master-thesis (used only in Table2)
```

*Table 1: Information for describing a device for vulnerability matching.*

| AAS | NetBox | CSAF | Description from AAS (mostly) | Relevant for CSAF matching                     | Source |
|  -           |  - | -  |- | - | - |
| Manufacturer Name| [Manufacturer:Name](#manufacturer-name) | vendor | Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market |Yes | [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Part number| [DeviceType:part_number](#part-number) | sku |unique product identifier of the manufacturer, also called [article number](#idta-02006-2-0)| Yes |  [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Order Code| DeviceType:order_code | N/A | By manufactures issued unique combination of numbers and letters used to identify the device for ordering. | No | [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Product Designation | :question: device:comments | optional [/document/notes_t/ (line 340-400)](https://github.com/oasis-tcs/csaf/blob/master/csaf_2.0/json_schema/csaf_json_schema.json) | short description of the product, product group or function | No | [IDTA 02003 1 2](#idta-02003-1-2) |
| Manufacturer Product Root| :question: deviceType:Role | N/A | Top level of a 3 level manufacturer specific product hierarchy (e. g. flow meter) | No | [IDTA 02006-2-0](#idta-02006-2-0)  |
| Manufacturer Product Family | [DeviceType:family](#device-family) | product_family |2nd level of a 3 level manufacturer specific product hierarchy | yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| Manufacturer Product Type | [DeviceType:model](#model-number)| product_name | Characteristic to differentiate between different products of a product family or special variants. :information_source: One of the two properties Manufacturer `Product Family` or Manufacturer `Product Type`  must be provided according to EU Machine Directive 2006/42/EC.| Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| *unknown* | [device:Description](#device-description) | x_generic_uris | :information_source: own additional level to a 3 level manufacturer specific product hierarchy| Yes | *unknown* |
| serial number| [Device:serial_number](#serial-number) | serial_number |unique combination of numbers and letters used to identify the device once it has been manufactured | Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| Year of Construction| [Device:YoC](#year-of-construct) | N/A| year as completion date of object | Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| Date of Manufacture| N/A | N/A| Date from which the production and / or development process is completed or from which a service is provided completely |No | [IDTA 02006-2-0](#idta-02006-2-0) |
| HardwareVersion| DeviceType:hardware_version| product_version and product_version_range| :information_source: [Version](#version-number)  of the hardware supplied with the device|Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| FirmwareVersion| [Software:version](#version-number) + flag "is firmware"| product_version and product_version_range| :information_source: [Version](#version-number) of the firmware supplied with the device|Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| SoftwareVersion| [Software:version](#version-number)| product_version and product_version_range| :information_source: [Version](#version-number) of the software used by the device |Yes | [IDTA 02006-2-0](#idta-02006-2-0) |
| URI | [x_generic_uris](#x_generic_uris) | x_generic_uris |Unique global identification of the product using a universal resource identifier (URI)| Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| SoftwareType | [SoftwareType](#software-type) | N/A |The type of the software (category, e.g. Runtime, Application, Firmware, Driver, etc.) | Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| Version Name| [Software:version_name](#software-name) | x_generic_uris |The name this particular version is given (e. g. focal fossa) | Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
| Version Info| Version Info | N/A | Provides a textual description of most relevant characteristics of the version of the software | No | [IDTA 02007-1-0](#idta-02007-1-0) |
| Manufacturer Name | [Manufacturer Name](#manufacturer-name)  | vendor in product_tree for this specific product| Creator of the software | Yes | [IDTA 02007-1-0](#idta-02007-1-0) |
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

## Discussion Device Type

The problem with the core field in Netbox for Device Type is that the model is unique and also the full identification for the device type. This leads to problems, when describing a device with [CSAF](https://csaf.io), since there is more than just a model (name) such as product family, product name and a stock keeping unit (sku) as illustrated with the following example:

| attribute | Netbox | DDDC |
|:---:|:----:|:---:|
| manufacturer | Rockwell Automation| Rockwell Automation|
| family | N/A | ControlLogix |
| model (number) | ControlLogix Rack K - 10 Slot| Rack K -10 Slot|
| part_number | 1756-A10K | 1756-A10K (sku)|
| | | |

### Device Family

#### device family Netbox

Not available. It is a part of the model name.

#### device family DINA

Text field added to the Device Type object. Specifies the family of a model (device type) (e.g. SIMATIC, SCALANCE) is assigned to.

### model number

#### model number Netbox

In Netbox the name convention is a little bit misleading, since under [devicetype-library](https://github.com/netbox-community/devicetype-library) a `model` is defined as :

```text
The model number of the device type. This must be unique per manufacturer.
```

So the object `model` is the model name as well as model number.

#### model number DINA

A model number can be used as an article number. However, an article number is not always/necessarily a model number. Usually, all products have model numbers, often they are listed on the sticker on the device besides the serial number

#### model number CSAF

```text
The terms "model", "model number" and "model variant" are mostly used synonymously. Often it is abbreviated as "MN", M/N" or "model no.".
```

### part number

#### Netbox part number

```text
An alternative representation of the model number (e.g. a SKU). 
```

#### part number - CSAF

CSAF defines the product identification helper [SKU](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31337-full-product-name-type---product-identification-helper---skus):

```text
Any given stock keeping unit of value type string with at least 1 character represents a full or abbreviated (partial) stock keeping unit (SKU) of the component to identify. Sometimes this is also called "item number", "article number" or "product number".
```

#### part number - DINA

It can be the same as model_number, especially when seller is the vendor itself. This can be used as an alternative presentation of the model number [e.g. SKU as in devicetype-library](https://github.com/netbox-community/devicetype-library).

## Approach 2 Recursiv DeviceTypes

There is an additional problem: manufacturers do not have a common level of the product hierarchy. This might also be the reason why level 2 is not clearly described in the IDTA.

Instead of extending the DeviceType classification, the current design of a DeviceType should remain unchanged. Only one additional field would be required:

- Is the DeviceType a child of another DeviceType?

In this way, the variable depth of manufacturers' product descriptions can be displayed.

```plaintext
Manufacturer
├── product family A
│   └── product of family A
│       ├── further specification
│       │   └── final specification (part number)
│       └── further specification
│           └── ...
├── product family B
    └── product of family B
        ├── further specification
        │   └── ...
        └── further specification
            └── final specification (part number) 
```

Always use the model name for the description of model, submodel or specification. In that way

- 1st model name describes the product family,
- 2nd model name can be used to differentiate between different products of this family,
- 3th model name can be used to differentiate between different specifications or sub products of this product.

In addition, the part number can also include the hardware version. This makes an additional custom field obsolete.
