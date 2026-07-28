# Roles

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](datamodel_idta.md)

---

## Purpose

The use case and reason for the implementation of parent/child relationship for roles is based on the [following issue #18245](https://github.com/netbox-community/netbox/issues/18245)

```text
In an environment where there are a lot of different device roles, it may be useful to be able to group them much like in the same way Tenants and Tenant Groups, or Contacts and Contact Groups are grouped today.

I can envisage that (for example) you may have a "Rack Infrastructure" Device Role Group which then has roles specific for "Patch Panel", "Power" etc.

Another example may be Network Switches, where you may want to segregate the Device Role based on function, while keeping them all under a Network Switch parent group.
```

Also, this feature can be used to group device roles for machine learning approach when not enough data is provided for a single device role but for a group.  

## Revision

There will be never THE definitive role structure. However, it should be reasonable and acceptable as well as adaptable.

|Sign               | Action                        |
|---                |                           --- |
|:question:         | group not sure, need reason   |
|:exclamation:      | need (clearer) description    |
| :skull:           | intended group is wrong 💀    |
|:no_entry_sign:    | role not helpful 🚫           |
|:white_check_mark: | ready for revision ✅         |

After revision the following tasks can be provided by `lazy.py` script in utils folder

- set color
- every role has all attributes: name, slug, parent, description, reason, color, vm_role

### Role Structure

> Please be aware when changing the following table that the structure of `device_role.yaml` will be set by the `|` sign.

```markdown
Primary device role
├── Field device
│   ├── Actuator ✅
│   ├── IIoT ❓
│   ├── Physical Sensor ✅
│   ├── NFC Reader ✅
│   └── VFD ✅
├── Controller
│   ├── CNC ✅
│   ├── IED ✅
│   ├── PLC ✅
│   └── RTU ✅
├── IT-Server✅
│   ├── Communication ✅
│   │   ├── Mail server ✅
│   │   ├── real time communication server ✅
│   │   ├── VPN server✅
│   │   ├── Web server✅
│   ├── Data Storage
│   │   ├── Cloud server ❓
│   │   ├── Data server 🚫
│   │   ├── File server ✅
│   │   ├── Historian✅
│   │   ├── Media server ✅
│   │   └── NAS ✅
│   ├── Administration ✅
│   │   ├── Active directory
│   │   ├── Application server ❓
│   │   ├── Authentication server ❓
│   │   ├── Domain controller ❓
│   │   └── SIEM ❓
│   ├── Management
│   │   ├── BMS ❓
│   │   ├── Collaboration server ❓
│   │   ├── PIMS ✅
│   │   ├── PLM ✅
│   │   └── VCS ✅
│   ├── Virtual Host Device ❓
│   │   ├── Hypervisor ✅
│   │   └── Virtual Machine Server ✅
│   └── Network Service
│       │── DHCP server ✅
│       │── DNS server ✅
│       │── Load balancer ✅
│       │── NTP server ✅
├── Network Structure::Magenta Pink
│   ├── Access point ✅
│   ├── Bridge ✅
│   ├── Hub ✅
│   ├── Network Proxy ✅
│   ├── Repeater ✅
│   ├── Switch L2 ✅
│   ├── Switch unspecified ✅
│   ├── KVM ❓
│   └── Gateway
│       │── Router ✅
│       │── Switch L3 ✅
│       │── Firewall ✅
│       │── Protocol-Coupler ✅
│       │── Modem ✅
├── SCADA
│   ├── Building Automation System ✅
│   │    ├── HVAC ✅
│   │    ├── Lighting control ✅
│   │    ├── Access Control
│   │       │── Camera ❓
│   │       │── Electronic access control ✅
│   ├── DCS ✅
│   ├── PCS ✅
├── OT-Client
│   ├── EWS ✅
│   ├── HMI ✅
│   ├── SCADA Client ❓
│   └── Workstation ❗🚫❓
├── Office
│   ├── Photocopier ✅
│   ├── Printer ✅
│   ├── print server ❓
│   └── Telephony ✅
│       │── Fax ✅
│       │── Phone ✅
├── Connected Device ✅
│   ├── IoT ✅
│   └── Kiosk ✅
├── Monitoring ✅
│   ├── IDS ✅   
│   ├── IPS ✅
│   ├── Network sensor ✅
│   └── Honeypot ✅
├── Unspecified ✅
│   └── MES ❓
```

### Role Color

#### Option 1

Note that the color of each device can be set using the `lazy.py` script with the `set_color` function. The color scheme can be configured via the `device_roles_colortemplate.json` file. The basic assumption is:

- the main device roles have their own color
- the children of a parent have the same color (darker)
- the offspring/descendent color becomes darker with each generation

#### Option 2

Use the `set_role_color_by_csv_mark`function in `lazy.py` to create device_roles from markdown structure and `color.csv`.
