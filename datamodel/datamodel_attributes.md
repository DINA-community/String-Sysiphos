# Attributes of data model

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](Discussion_datamodel.md)

---

## TODO

| Task   | Status    |
|-|-|
| check attribute description of NetBox| ok|
| data collection (tables) review by K. H.| open|
| CSAF | full product name|
| CSAF | Mapping klar mit NetBox kenntlich machen|
| Field und Action trennen | open |
| Link zu Attributen in allen Dokumenten| open |

add purpose to each attribute
purpose: for IDS, CSAF, vulnerability, critical operation
collection: passive (with DDDC and DeviceMgt) - marketing

qs: Such as is also used to clarify information in a statement.
A good way to remember how to properly use like or such as in a sentence is to remember that like is used in similes; it’s always used to compare something to something else. Such as can also be another way of saying including, since both can be used to list specific examples

## Device

Legend for possible sources

```markdown
* :computer: = PCAP
* :mag: = DeviceMgt
* :calling: = Active requests to device/system
* :construction_worker:= Manual by user
```

| **Device**                            | Main source (possible source)         |
|-                           |  -                                    |
| [backup](#backup-frequency--type)                             | :construction_worker:                 |
| [baseline image](#baseline-image)                             | :construction_worker:                 |
| [criticality](#criticality)                                   | :construction_worker:                 |
| [date of manufacture](#date-of-manufacture)                   | :construction_worker:                 |
| [device key](#device-key)                                     | :question:                            |
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
| [serial number](#serial-number)                               | :construction_worker: (:calling: )    |
| [site](#site)                                                 | :construction_worker: (:computer:)    |
| [time source](#time-source)                                   | :construction_worker: (:computer:)    |
| [user accounts](#user-accounts)                               | :construction_worker: (:computer:)    |
| [vlan](#vlan)                                                 | :calling:                             |
| [virtual](#virtual)                                           | :construction_worker:, :question:     |

### Backup Frequency / Type

This attribute provides frequency for how often backups are performed (e.g., daily, weekly, monthly) and method used (e.g., full, incremental, differential).

### Baseline Image

Useful to know if there is a particular known-good image that the OS installation was based on, aiding in post-incident recovery

### Criticality

Enables device to be managed based on its operational role, safety impact, and/or exposure to risks.

### Date of Manufacture

This information might be relevant for legacy products when mapping against new information where the product is renamed or listed under a new vendor. Also, it can be used to determine the obsolescence of the device.

### Device key

Unique identifier assigned to the asset by the organization

### Device name

Text field containing the descriptive name of the device.
Potentially useful for understanding context and function of the device in the network if included in host naming conventions.

### Exposure

Selection added to the Device Type object. Specifies the grade of exposure to other networks. Valid values are:

- Small:  The asset is in a highly isolated and controlled zone. There are no connections from this cyber asset’s zone to or from a zone with lower trust.
- Indirect: The asset has no direct access to a zone with lower trust, but other cyber assets in this cyber asset’s zone are accessible to or from a zone with lower trust.
- Direct: The asset is directly accessible to or from a zone with lower trust.
- Unknown: Value if category for exposure is unknown.  

### Hostname

see Device Name

### Hypervisor

If applicable, this attribute provides context in what type of hypervisor is running the VM

### Hypervisor (Location within)

This attribute provides context on where the VM resides within the hypervisor

### Location

GPS coordinates of the device for geo location. [NetBox](https://netboxlabs.com/docs/netbox/en/stable/models/dcim/location/)

### MAC address

Useful for determining manufacturer, if not otherwise specified.  
**Note**: Could only refer to network card manufacturer

### Operation Status

The device's operational status.

### Owner

Useful in understanding who owns or is responsible for the machine

### Rack

The [rack](<https://netboxlabs.com/docs/netbox/en/stable/models/dcim/rack/>) within which this device is installed (optional).

### Role (primary)

Useful for understanding context and function of the device in the network.  
Note: Be aware, that with [NetBox 4.3](https://netboxlabs.com/docs/netbox/en/stable/release-notes/version-4.3/#hierarchical-device-roles-18245) roles can be child or parent (optional). For instance a firewall now can be a child of a gatway.

### Role (secondary)

Multiple objects field added to the Device object. It should be possible to assign multiple Device Roles to a device. Therefore, this custom field enables the user to designate multiple Device Roles for a device using this feature. Additionally, the existing ’Role’ attribute of a device should be understood as the primary role of the device. For instance, a primary role of a S7-1200 can be PLC and a secondary role a bus coupler.

### Safety

Boolean field added to the Device object. Specifies, if the device is used/provides safety functionality.

### Serial Number

Text field for the serial number of the device. Helps to determine the affectedness. For example, a batch (SN range) has been shipped with a FW that contains a vulnerability.

### Site

Specifies the name of the site in which the device is located.
<https://netboxlabs.com/docs/netbox/en/stable/models/dcim/site/>

also Useful when conducting user behavior analysis where timelines come into play (local time zone)

### Time Source

This attribute provides clarity on how an asset synchronizes its operations (e.g. NTP, GPS, Atomic Clock, Local Clock, etc...) as disruption of an external time source and associated drift could result in significant impacts.

### User Accounts

Useful in knowing which user account is expected to be most active, or if it’s expected to be accessed by many different users

### VLAN

Useful for understanding its grouping on the network.

### Virtual

Is the asset physical or virtual.

## Device Type

The device type can be represented with many attributes. Instead of using only one field, this data model uses several fields to record the product hierarchy. The discussion on [NetBox community](https://github.com/netbox-community/netbox/discussions/14125)\

| **Device Type**   | -    |
|-|-|
| [cpe](#cpe)                                           | :construction_worker:     |
| [device family](#device-family)                       | :mag:                     |
| [device type description](#device-type-description)   | :construction_worker:     |
| [hardware name](#hardware-name)                       | :calling:                 |
| [hardware version](#hardware-version)                 | :calling:                 |
| [manufacturer](#manufacturer-of-device-type)          | :mag:                     |
| [model](#model)                                       | :calling:                 |
| [part number](#part-number)                           | :calling:                 |

### CPE

Text field added to the Device Type object. It specifies the Common Platform Enumeration (CPE) string of the device type.

### Device Family

It is usually family a model is assigned to.

### Device Type Description

Additional, optional field for detailed information regarding the model description or purpose of this particular device type in the operation site.
It can be used as an additional reminder alongside the device type name (e.g. CPU 414-3 PN/DP central unit with 4 MB RAM...). Could be partially part of full_product_name_t/name in a CSAF document.

### Hardware Name

Further specification of device type. It is usually the product name of manufacturer like `S7-1515f`? @mrt

### Hardware Version

Point of purchase (may not be manufacturer)
Multiple products exist in multiple hardware versions (due to PCB layout changes or chip shortages or hardware improvements), which can have impact on the software that can be used with the device.

### Manufacturer of Device Type

Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging
and labeling of a product in respect to its being brought into the market.\[[IDTA 02003 1 2](https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02003-1-2_Submodel_TechnicalData.pdf)\].

### Model

Model is the specification of device_family.
A model number can be used as an article number. However, an article number is not always/necessarily a model number. Usually, all products have model numbers. Often they are listed on the sticker on the device besides the serial number.

### Part Number

Part number specifies the stock keeping unit (SKU). It can be the same as model number (NetBox:
part_number), especially when seller is the vendor itself. In [CSAF](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31337-full-product-name-type---product-identification-helper---skus) it is mentioned that the sku sometimes called "item number", "article number" or "product number".

## Service (check the plugin usecase! TODO)

By services the interaction within the IT/OT and outside the perimeter is documented.

| **Service**                             |   Main source (possible source) |
|-                                                          |   -           |
| [Communication partner IP](#communication-partner---ip)   | :computer:    |
| [protocol](#protocolservices)                             | :computer:    |
| [ports](#portsservices)                                   | :computer:    |

### Communication partner - IP

Not all observed CP have to be expected ones. This entry serves as baseline (truth of state) for IDS

### Protocol/Services

A [service](https://netboxlabs.com/docs/netbox/en/stable/models/ipam/service/) represents a layer seven application available on a device or virtual machine. For example, a service might be created in NetBox to represent an HTTP server running on TCP/8000. Each service may optionally be further bound to one or more specific interfaces assigned to the selected device or virtual machine. As protocol there are the option UDP, TCP and SCTP.\
The type of the protocol such as transport, application oder network, can be described using the description field.

### Ports/Services

The port number of a service can be used to determine the protocol type if unknown as well as a possible role of the device.\

## Software

| **Software**          | Main source (possible source) |
|-|-|
| [manufacturer](#firmware-manufacturer)            | :calling: (:construction_worker:) |
| [software type](#software-type)                   | :calling: (:construction_worker:) |
| [software name](#software-name)                   | :calling: (:construction_worker:) |
| [software version](#software-version)             | :calling: (:construction_worker:) |
| [software version name](#software-version-name)   | :calling: (:construction_worker:) |
| [software manufacturer](#software-manufacturer)   | :calling: (:construction_worker:) |
| [firmware name](#firmware-name)                   | :calling: (:construction_worker:) |
| [firmware version](#firmware-version)             | :calling: (:construction_worker:) |
| [firmware version name](#firmware-version-name)   | :calling: (:construction_worker:) |
| [firmware manufacturer](#firmware-manufacturer)   | :calling: (:construction_worker:) |
| [operating system](#operating-system)             | :calling: (:construction_worker:) |
| [operating version](#operating-system-version)    | :calling: (:construction_worker:) |
| [operating version name](#operating-system-version-name) | :calling: (:construction_worker:) |
| [cpe](#cpe-software)                              | :construction_worker:   |
| [hashes](#hashes)                                 | :construction_worker:   |
| [purl](#purl)                                     | :construction_worker:   |
| [sbom_urls](#sbom--urls)                          | :construction_worker:   |
| [x_generic_uris](#x_generic_uris)                 | :construction_worker:   |

The fields for characterizing the software and respectively firmware are as follows:

```bash
software_name: "Debian"
software_version: "12.6"
software_version_name: "Bookworm"
```

### Software Type

It has to be distinguished between firmware and additional software by the flag "is firmware".

### Software Name

list of additional software
Examples: OS like Linux or libraries in python.

### Software Version

The name this particular version is given.  
:information_source: There are plenty of valid notations for version schema. Therefore, there is no common standard.

TODO

In the latter case, it is recommended to use the version range specifier [vers](https://github.com/package-url/purl-spec/blob/version-range-spec/VERSION-RANGE-SPEC.rst).

### Software Version Name

Provides a textual description of most relevant characteristics of the version of the software

### Software Manufacturer

Manufacturer of the software, not hardware. In case of firmware, this usually be the manufacturer of the device. @mrt

### Firmware Name

Firmware (FW) of device, not of installed software (flag must be set in NetBox). The firmware
interacts directly with the hardware.

### Firmware Version

FW of device, not of installed software (flag must be set in NetBox).
Hash for firmware SHA256 or SHA512 (preferred) would be appropriate. Otherwise use plan text such as  "Version 8.2.x"

### Firmware Version Name

FW of device, not of installed software (flag must be set in NetBox)
Provides a textual description of most relevant characteristics of the version of the software

### Firmware Manufacturer

manufacturer of the firmware, not hardware. In case of firmware, this usually be the manufacturer of the device. @mrt

### Operating System

The question here is whether an operating system (by definition) is not already too big to be firmware. The boundaries will certainly become blurred in practice - so the firmware of a PLC could be described as its operating system.

### Operating System Version

Hash SHA256 or SHA512 (preferred) would be appropriate. Otherwise use plan text such as  "Version 8.2.x"

### Operating System Version Name

Provides a textual description of most relevant characteristics of the version of the operating system.

### CPE Software

It specifies the Common Platform Enumeration (CPE). Text field added to the Software/Firmware/OS (mrt ?) object. CPE attribute refers to a method for naming platforms external to this specification (see [CPE23](https://dx.doi.org/10.6028/NIST.IR.7695) for details).
Note: CPE 2.2 and 2.3 version are not clear regarding HW or FW.

### Hashes

Hashes should be used for firmware and applications software.
Tuple [(hash(alg, file), file)], sind ca. 7 Hashwerte @mrt explain
Hash for firmware SHA256 or SHA512 (preferred) would be appropriate. Otherwise use plan text such as  "Version 8.2.x"

### Purl

The package URL (PURL) refers to a method for reliably identifying and locating software packages external to this specification [PURL](https://github.com/package-url/purl-spec).

### SBOM  URLs

The URL is a unique identifier. The content is secondary. The SBOMs might differ in format or depth of detail. Currently, [CSAF 2.0](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#31335-full-product-name-type---product-identification-helper---sbom-urls) supported formats are SPDX, CycloneDX, and SWID.

### x_generic_uris

Unique name given by the vendor.The TC provides some [examples](https://github.com/oasis-tcs/csaf/issues/649). Hardware and software, can have one or more x_generic_uri. However, an x_generic_uri can only belong to one hardware resp. software.
