# Roles

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](Discussion_datamodel.md)

---

## Purpose

The use case and reason for the implementation of parent/child relationship for roles is based on the [following issue #18245](https://github.com/netbox-community/netbox/issues/18245)

```text
Use case

In an environment where there are a lot of different device roles, it may be useful to be able to group them much like in the same way Tenants and Tenant Groups, or Contacts and Contact Groups are grouped today.

I can envisage that (for example) you may have a "Rack Infrastructure" Device Role Group which then has roles specific for "Patch Panel", "Power" etc.

Another example may be Network Switches, where you may want to segregate the Device Role based on function, while keeping them all under a Network Switch parent group.

```text

Also, this feature can be used to group device roles for machine learning approach when not enough data is provided for a single device role but for a group.  

There are open task in the corresponding `device_roles.yml`:

 - color in relation to parent role
 - reason fields that contains open questions

### Role Structure

```text
Primary device role
├── Field device
│   └── Actuator
│   └── IIoT
│   └── Physical Sensor
│   └── Scanner
│   └── VFD
├── Controller
│   └── CNC
│   └── IED
│   └── PLC
│   └── RTU
├── IT-Server
│   └── Communication
│       └── Mail server
│       └── Proxy server
│       └── RTC
│       └── VPN server
│       └── Web server
│   └── Storage
│       └── Cloud server
│       └── Data server
│       └── File server
│       └── Historian
│       └── Media server
│       └── NAS
│   └── Service A
│       └── Active directory
│       └── Application server
│       └── Authentication server
│   └── Management
│       └── BMS
│       └── Collaboration server
│       └── PIMS
│       └── PLM
│       └── SIEM
│       └── VCS
│   └── Service B
│       └── Hypervisor
│       └── Load balancer
│       └── NTP server
│       └── Virtual Machine Server
│   └── Service C
│       └── DHCP server
│       └── DNS server
│       └── Domain controller
├── Network Structure
│   └── Access point
│   └── Bridge
│   └── Gateway-Coupler
│   └── Hub
│   └── Modem
│   └── Repeater
│   └── Switch L2
│   └── Switch unspecified
├── SCADA
│   └── BAS
│   └── DCS
│   └── PCS
├── OT-Client
│   └── EWS
│   └── HMI
│   └── SCADA Client
│   └── Workstation
├── Office
│   └── KVM switch
│   └── Photocopier
│   └── Printer
│   └── Server
│       └── printer server
│   └── Telephony
│       └── Fax
│       └── Phone
├── Building automation
│   └── HVAC
│   └── Lighting controls
│   └── Access Control
│       └── Camera
│       └── Electronic access control
├── Connected Devices
│   └── Camera
│   └── IoT
│   └── Kiosk
├── Monitoring
│   └── IDS   
│   └── IPS
│   └── Network sensor
├── Gateway
│   └── Router
│   └── Switch L3
├── Unspecified
```
