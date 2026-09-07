# Attributes of data model

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](datamodel_idta.md)

---

## Introduction

An OT asset inventory — an organized, regularly updated list of an organization’s OT systems, hardware, and software — is foundational to designing a modern defensible architecture because without an inventory, organizations do not know what they have and what should be secured and protected.
Successful asset management requires knowing what data needs to be captured for each asset in an inventory. This page lists recommended fields for the asset inventory and the potential benefits of including them. It enriches and explains fields listed in [Foundations for OT Cybersecurity: Asset Inventory Guidance for Owners and Operators - Appendix A](https://www.cisa.gov/resources-tools/resources/foundations-ot-cybersecurity-asset-inventory-guidance-owners-and-operators).

The goal is to know what the asset does and where it is located. This means that not only technical data is needed, but also metadata to understand the purpose of the asset. This is the only way to derive attributes such as criticality.

Furthermore it has to be kept in mind that not all attributes have the same priority. Also a broader incomplete database is better than having only a few assets described fully and the rest is missing (almost) completely.

In addition, the most likely source for capturing this information is indicated at the beginning of each section. The sections are [`device`](#device), [`device type`](#device-type) and [`software`](#software).

### Legend for possible sources

* :computer: = PCAP
* :mag: = DeviceMgt
* :calling: = Active requests to device/system
* :construction_worker:= Manual by user (using bulk function when possible)

Collecting data should be automated as much as possible. However, the source of truth only can be provided by qualified personal who know the facility.

## Device

| **Device**                                                    | Main source (possible source)         |  
|-                                                              |  -                                    |
| [asset identifier](#asset-identifier)                         | :construction_worker:                 |
| [backup](#backup-frequency--type)                             | :construction_worker:                 |
| [baseline image](#baseline-image)                             | :construction_worker:                 |
| [configuration](#configuration)                               | :construction_worker:                 |
| [criticality](#criticality)                                   | :construction_worker:                 |
| [date of manufacture](#date-of-manufacture)                   | :construction_worker:                 |
| [device name](#device-name)                                   | :computer:                            |
| [exposure](#exposure)                                         | :construction_worker: (:computer:)    |
| [hostname](#hostname)                                         | :computer:                            |
| [hypervisor](#hypervisor)                                     | :construction_worker:                 |
| [hypervisor(location within)](#hypervisor-location-within)    | :construction_worker:                 |
| [location](#location)                                         | :construction_worker:                 |
| [mac_address](#mac-address)                                   | :computer:                            |
| [operation status](#operation-status)                         | :computer:                            |
| [owner](#owner)                                               | :construction_worker:                 |
| [rack](#rack)                                                 | :construction_worker:                 |
| [role primary](#role-primary)                                 | :construction_worker: (:mag:)         |
| [role secondary](#role-secondary)                             | :construction_worker:                 |
| [safety](#safety)                                             | :construction_worker:                 |
| [security level](#security-level)                             | :construction_worker:                 |
| [serial number](#serial-number)                               | :construction_worker: (:calling: )    |
| [site](#site)                                                 | :construction_worker: (:computer:)    |
| [time source](#time-source)                                   | :construction_worker: (:computer:)    |
| [time zone](#time-zone)                                       | :construction_worker: (:computer:)    |
| [user accounts](#user-accounts)                               | :construction_worker: (:computer:)    |
| [vlan](#vlan)                                                 | :computer: (:calling:)                |
| [virtual](#virtual)                                           | :construction_worker:,                |

### Asset Identifier

Unique identifier assigned to the asset by the organization.

### Backup Frequency / Type

This attribute provides frequency for how often backups are performed (e.g., daily, weekly, monthly) and method used (e.g., full, incremental, differential).

### Baseline Image

It is useful to know if there is a particular known-good (baseline) image that the OS installation was based on, aiding in post-incident recovery.

### Configuration

It is a generic term that contains a URI to one or more configuration files. Those files can be the full configuration, the changelog for device attributes, or even the configuration of communication partners in further detail, such as a Substation Configuration Descriptor (SCD) file.

### Criticality

Assets are classified based on their importance to the organization's operations, safety, and mission as well as the exposure to risks.
Critical assets are those whose failure or compromise would have the most significant impact. One approach to determine those is the
[Consequence-Driven Cyber-Informed Risk Assessment Exercises](https://ci-discern.com/cce-risk-assessment)

### Date of Manufacture

This information might be relevant for legacy products when mapping against new information where the product is renamed or listed under a new vendor. Also, it can be used to determine the obsolescence of the device.

### Device Description

Detailed device description such as specific hardware configuration.
> Note: The purpose of the device should be clear by the device role.

### Device name

A device usually has a descriptive name given by the manufacturer, integrator or operator ("Well known name"). It can be
potentially useful for understanding context and function of the device in the network if included in host naming conventions like A1SETT01 for \<Site>\<Type>\<Role>\<ID\> meaning Area1, Sensor, Temp. Transmitter and ID 01.

### Exposure

Specifies the grade of exposure to other networks of a device. Valid values are:

* Small: The asset resides in a highly isolated and controlled zone. There are no conduits with a zone of lower trust.
Neither this asset can access lower-trust zones nor can it be accessed by them.
* Indirect: The asset itself has no direct conduits with a zone of lower trust.
However, other assets in the same zone can be accessed from, or can access, zones with lower trust — creating a potential indirect exposure path.
* Direct: The asset has direct conduits to or from a zone of lower trust.
* Unknown: The exposure level of the asset is currently undetermined.  

### Hostname

see [Device Name](#device-name)

### Hypervisor

If applicable, this attribute provides context in what type of hypervisor is running the VM.  
:question: *This attribute needs further specification. Why and for what is this attribute useful*

### Hypervisor (Location within)

This attribute provides context on where the VM resides within the hypervisor.  
:question: *This attribute needs further specification. Why and for what is this attribute useful*

### Location

Racks and devices can be grouped by location within a site. A location may represent a floor, room, cage, or similar organizational unit. Locations can be nested to form a hierarchy. For example, you may have floors within a site, and rooms within a floor. [NetBox](https://netboxlabs.com/docs/netbox/models/dcim/location/)
Besides a text description, GPS coordinates of the device for geo location can be used.

### MAC address

Useful for determining manufacturer, if not otherwise specified.  
**Note**: Could only refer to network card manufacturer

### Operation Status

The device's operational status.

* Offline
* Active
* Planned
* Staged
* Failed
* Inventory
* Decommissioning

### Owner

This attribute is useful in understanding who owns or is responsible for the machine.

### Rack

The [rack](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/rack/) within which this device is installed. It determines the [location](#location) further.

### Role (primary)

Useful for understanding context and function of the device in the network (see [Roles](datamodel_roles.md)).  
> Note: Be aware, that with [NetBox 4.3](https://netboxlabs.com/docs/netbox/en/stable/release-notes/version-4.3/#hierarchical-device-roles-18245) roles can be child or parent (optional). For instance a firewall now can be a child of a gateway.

### Role (secondary)

There can be multiple additional roles for a device. For instance, a primary role of a Siemens S7-1200 can be PLC and a secondary role a bus coupler.

### Role of Responsible Person

A role such as system operator.
> Deprecated: *This attribute provides no useful content.*

### Safety

This attribute specifies if the device is used/provides safety functionality.

### Security level

The security level is determined by a risk analysis. Therefore, relevant information like exposure, possible safety function and role of the device should be collected systematically for all devices.

### Serial Number

Unique combination of numbers and letters used to identify the device once it has been manufactured [IDTA 2006](datamodel_idta#idta-02006-2-0).
It helps to determine the affectedness by vulnerabilities. For example, a batch (SN range) has been shipped with a FW that contains a vulnerability.  
Also, it can be used to check the device identity.

### Site

Specifies the name of the site in which the device is located.

[NetBox Definition](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/site/):

``` text
How you choose to employ sites when modeling your network may vary depending on the nature of your organization, but generally a site will equate to a building or campus. For example, a chain of banks might create a site to represent each of its branches, a site for its corporate headquarters, and two additional sites for its presence in two colocation facilities.
```

### Time Source

This attribute provides clarity on how an asset synchronizes its operations (e.g. NTP, GPS, Atomic Clock, Local Clock, etc...) as disruption of an external time source and associated drift could result in significant impacts.

### Time Zone

This attribute can be useful when conducting user behavior analysis where timelines come into play (local time zone). It must to be clear whether the value is an hourly deviation from UTC or a shift in another time scale (minutes or seconds). Furthermore, it should be clear whether and how summer time is to be applied.

### User Accounts

An array of legitime user accounts. This makes it easier to identify unknown accounts. Using this information further, the behavior of each account (when an account is expected to be used and how often) in order to create appropriate IDS signatures.

### VLAN

Useful for understanding its grouping on the network. However, it should be clarified how to handle switches in this context.

### Virtual

Is the device physical or virtual.  
:question: *This attribute needs further specification. Why and for what is this attribute useful*

## Device Type

> **Note:** In this section, device types also represent module types, which are introduced in the NetBox data model.

A device type can be described by many attributes. Instead of relying on a single field, this data model uses several fields to record the product. This statement is also valid for module types. As stated in the [NetBox documentation](https://netboxlabs.com/docs/netbox/models/dcim/module/):

> "A module is a field-replaceable hardware component installed within a device that houses its own child components. Similar to devices, modules are instantiated from module types, and any components associated with the module type are automatically instantiated on the new model."

In OT environments, a module type family such as SIPLUS ET can have different modules, for example interface and supply modules.

Both types are useful for determining whether a product is affected by a vulnerability. Additionally, the modules used in a device may indicate its function.

### Representing Types

#### Recursive Hierarchy

The preferred way to do this would be a recursive structure (see discussion on [NetBox community](https://github.com/netbox-community/netbox/discussions/14125)). In this way, the different description in depth of manufacturers could be handled in a clear structure which is similar to the CSAF:

```plaintext
Manufacturer
├── product family A
│   └── product of family A
│       ├── further specification
│       │   └── final specification
│       └── further specification
│           └── ...
├── product family B
    └── product of family B
        ├── further specification
        │   └── ...
        └── further specification
            └── final specification 
```

* 0st describe the manufacturer,
* 1st describe the product family,
* 2nd distinguish between different products of this family,
* 3th distinguish between different specifications or sub products of this product or versions

This approach from a data base point of view is more complex. Therefore, the plain hierarchy is used instead.

#### Plain Hierarchy

Using a fix number of attributes to describe the device type, the preferred structure in context to CSAF and NetBox is:

| Attribute                 |  Device Type                          |  Module Type                          |
|:-------------------------:|:-------------------------------------:|:-------------------------------------:|
| manufacturer              | Rockwell Automation                   | Siemens                               |
| family                    | ControlLogix                          | SIPLUS ET                             |
| model (number)            | Rack K -10 Slot                       | 200 SP                                |
| part_number               | 1756-A10K                             | 6AG2155-6AU01-4CN0                    |
| hardware name             | N/A                                   | IM 155-6 PN                           |
| hardware version          | 1.0                                   | 4.12.0                                |
| type description          | detailed specification of GPU and RAM | HF TX RAIL                            |
|                           |                                       |                                       |

This solution is simpler and more user-friendly option across databases. However, a significant portion of product-specific information may be stored in the description field, which could complicate the mapping process.

| **Device/Module Type**                                | -                         |
|-                                                      |-                          |
| [cpe](#cpe)                                           | :construction_worker:     |
| [device family](#device-family)                       | :mag:                     |
| [device type description](#device-type-description)   | :construction_worker:     |
| [hardware name](#hardware-name)                       | :calling:                 |
| [hardware version](#hardware-version)                 | :calling:                 |
| [lifecycle status](#lifecycle-status)                 | vendor                    |
| [manufacturer](#manufacturer-of-device-type)          | :mag:                     |
| [model](#model)                                       | :calling:                 |
| [part number](#part-number)                           | :calling:                 |
| [patch cycle](#patch-cycle)                           | :construction_worker:     |

### CPE

It specifies the Common Platform Enumeration (CPE) string of the device type by the manufacturer.

### Device Family

It is usually a family a model (e.g. SIMATIC, SCALANCE) is assigned to. Also, a device family can be a child of a device family (see below). Here a hierarchy would be a proper way representing it (see also [netbox discussion #14125](https://github.com/netbox-community/netbox/discussions/14125)).

| manufacturer | product family (parent) | product family (child)| product family (grandchild)|  model-number  | part number |
| -- |--         | -- | -- | -- |--|
| Siemens | SCALANCE| SC-600 | SC622-2C | specification A |(6GK5622-2GS00-2AC2)|
| Siemens | SCALANCE| SC-600 | SC622-2C | specification B |(6GK5622-2GS00-2BC2)|

### Device Type Description

Attribute for detailed information regarding the model description or purpose of this particular device type in the operation site.
It can be used as an additional reminder alongside the device type name (e.g. CPU 414-3 PN/DP central unit with 4 MB RAM...).

Also, it could be partially part of `full_product_name_t/name` in a CSAF document.

### Hardware Name

Further specification of device type. It is usually the product name of manufacturer like `S7-1515f`.

### Hardware Version

Multiple products exist in multiple hardware versions (due to PCB layout changes or chip shortages or hardware improvements), which can have impact on the software that can be used with the device.

### Lifecycle status

End-of-Life (EOL) and End-of-Support (EOS) information (see [OpenEoX](https://openeox.org/)). Knowing when a device type will reach the end of its service life, alternatives can be found and purchase to ensure business continuity

### Manufacturer of Device Type

Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging
and labeling of a product in respect to its being brought into the market.\[[IDTA 02003 1 2](https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02003-1-2_Submodel_TechnicalData.pdf)\].

### Model

Model is the specification of device_family.
A model (number/variant) can be used as an article number. However, an article number is not always/necessarily a model number. Usually, all products have model numbers. Often they are listed on the sticker on the device besides the serial number.

### Part Number

Part number specifies the stock keeping unit (SKU). It can be the same as model number (NetBox:
part_number), especially when seller is the vendor itself. In [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31337-full-product-name-type---product-identification-helper---skus) it is mentioned that the sku sometimes called "item number", "article number" or "product number".

### Patch cycle

The regular patch cycle of this kind of device type.

## Service

By services the interaction within the IT/OT and outside the perimeter is documented.

| **Service**                                               |   Main source (possible source)   |
|-                                                          |   -                               |
| [Communication partner IP](#communication-partner---ip)   | :computer:                        |
| [protocol](#protocolservices)                             | :computer:                        |
| [ports](#portsservices)                                   | :computer:                        |

### Communication partner - IP

Not all observed CP have to be expected ones. This entry serves as baseline (truth of state) for intrusion detection systems (IDS).

### Protocol/Services

A [service](https://netboxlabs.com/docs/netbox/en/stable/models/ipam/service/) represents a layer seven application available on a device or virtual machine. For example, a service might be created in NetBox to represent an HTTP server running on TCP/8000. Each service may optionally be further bound to one or more specific interfaces assigned to the selected device or virtual machine. As protocol there are the option UDP, TCP and SCTP.  
The type of the protocol such as transport, application oder network, can be described using the description field.
> Note: not observed communication partner protocol but expected one (source of state)

### Ports/Services

The port number of a service can be used to determine the protocol type if unknown as well as a possible role of the device.

## Software

| **Software**          | Main source (possible source) |
|-|-|
| [software cpe](#software-cpe)                              | :construction_worker:   |
| [software type](#software-type)                   | :calling: (:construction_worker:) |
| [software name](#software-name)                   | :calling: (:construction_worker:) |
| [software version](#software-version)             | :calling: (:construction_worker:) |
| [software version name](#software-version-name)   | :calling: (:construction_worker:) |
| [software manufacturer](#software-manufacturer)   | :calling: (:construction_worker:) |
| [hashes](#hashes)                                 | :construction_worker:   |
| [purl](#purl)                                     | :construction_worker:   |
| [sbom_urls](#sbom-urls)                           | :construction_worker:   |
| [x_generic_uris](#x_generic_uris)                 | :construction_worker:   |

> The fields for characterizing the software are also used for firmware and operating system respectively:

```bash
software_name: "Debian"
software_version: "12.6"
software_version_name: "Bookworm"
```

### Software CPE

It specifies the Common Platform Enumeration (CPE). CPE attribute refers to a method for naming platforms external to this specification (see [CPE23](https://dx.doi.org/10.6028/NIST.IR.7695) for details).

### Software Type

It has to be distinguished between firmware and additional software. This can be achieved by the flag "is firmware".

### Software Name

List of additional software on the device. Also, it could be an operating system like Linux.  
Firmware (FW) of device is not installed software. The firmware interacts directly with the hardware.  
The question here is whether an operating system (by definition) is not already too big to be firmware.  
The boundaries will certainly become blurred in practice - so the firmware of a PLC could be described as its operating system.

:question: *This attribute needs revision.*

### Software Version

The name this particular version is given.  
:information_source: There are plenty of valid notations for version schema such as [SemVer](https://semver.org/) or [CalVer](https://calver.org/).

### Software Version Name

This attribute provides a textual description of most relevant characteristics of the version of the software.

### Software Manufacturer

Manufacturer of the software, not hardware. In case of firmware, this can often be the manufacturer of the device.

### Hashes

Hashes should be used for firmware and applications software.
Tuple [(hash(alg, file), filename)] for firmware in SHA256 or SHA512 (preferred) would be appropriate.

### Purl

The package URL (PURL) refers to a method for reliably identifying and locating software packages external to this specification [PURL](https://github.com/package-url/purl-spec).

### SBOM URLs

The URL is a unique identifier. The content is secondary. The SBOMs might differ in format or depth of detail. Currently, [CSAF 2.0](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31335-full-product-name-type---product-identification-helper---sbom-urls) supported formats are SPDX, CycloneDX, and SWID.

### x_generic_uris

Unique name given by the vendor. The technical committee provides some examples \[[1](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31338-full-product-name-type---product-identification-helper---generic-uris), [2](https://github.com/oasis-open/csaf-documentation/blob/master/examples/x_generic_uris.md)\]. Hardware and software, can have one or more x_generic_uri. However, an x_generic_uri can only belong to one hardware resp. software.
