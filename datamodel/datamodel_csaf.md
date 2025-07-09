# Data model Mapping CSAF

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](Discussion_datamodel.md)

---

Only relevant attributes for CSAF are shown in the table. The revision is from NetBox version 3.7 to 4.3.

Legend

- (new Core): former custom field is now part of the core model
- (new): new custom field
- (custom field): Former custom field name, which is replaced

| **ASSET**                       | |
| ------------------------------- | ------------------------------------------------------------------------ |
| **DeviceType**                  |  **CSAF (JSON-Path)**|
| [`Manufacturer:name`](datamodel_attributes.md#manufacturer-of-device-type)              | - `$.product_tree..branches[?(@.category=="vendor")].name`|
| [`device_family`](datamodel_attributes.md#device-family)                  | - `$.product_tree..branches[?(@.category=="product_family")].name`|
| [`model_number (new)`]((datamodel_attributes.md#model) )            | - `$.product_tree.full_product_names[*].product_identification_helper.model_numbers[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.model_numbers[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.model_numbers[*]` |
| [`part_number (article_number)`](datamodel_attributes.md#part-number)  | - `$.product_tree.full_product_names[*].product_identification_helper.skus[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.skus[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.skus[*]`|
| [`hardware_version`](datamodel_attributes.md#hardware-version)               | - `$.product_tree..branches[?(@.category=="product_version")].name`<br>- `$.product_tree..branches[?(@.category=="service_pack")].name`<br>- `$.product_tree..branches[?(@.category=="patch_level")].name`<br>- `$.product_tree..branches[?(@.category=="product_version_range")].name`   |
| [`hardware_name (new)`](datamodel_attributes.md#hardware-name)           | - `$.product_tree..branches[?(@.category=="product_name")].name`  |
| [`device_description (new Core)`](datamodel_attributes.md#device-description) | - If matching by Full Product Name:<br>- `$.product_tree.full_product_names[*].name`<br>  - `$.product_tree..branches[*].product.name`<br>  - `$.product_tree.relationships[*].full_product_name.name`|
| [`cpe`](datamodel_attributes.md#cpe-software)                             | - `$.product_tree.full_product_names[*].product_identification_helper.cpe`<br>- `$.product_tree..branches[*].product.product_identification_helper.cpe`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.cpe`                                        |
| **Device**                      |   |
| [`name`](datamodel_attributes.md#device-name)                            | - `$.product_tree..branches[?(@.category=="host_name")].name`  |
| [`serial`](datamodel_attributes.md#serial-number)                        | - `$.product_tree.full_product_names[*].product_identification_helper.serial_number[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.serial_number[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.serial_number[*]` |
| **Software**                    |   |
| [`name`](datamodel_attributes.md#software-name)                          | - `$.product_tree..branches[?(@.category=="product_name")].name` |
| [`Manufacturer:name`](datamodel_attributes.md#software-manufacturer)    | - `$.product_tree..branches[?(@.category=="vendor")].name`  |
| [`version`](datamodel_attributes.md#software-version)                       | - `$.product_tree..branches[?(@.category=="product_version")].name`<br>- `$.product_tree..branches[?(@.category=="service_pack")].name`<br>- `$.product_tree..branches[?(@.category=="patch_level")].name`<br>- `$.product_tree..branches[?(@.category=="product_version_range")].name`                                                         |
| [`cpe`](datamodel_attributes.md#cpe)                          | *(see above under DeviceType)* |
| [`purl`](datamodel_attributes.md#purl)                         | - `$.product_tree.full_product_names[*].product_identification_helper.purl`<br>- `$.product_tree..branches[*].product.product_identification_helper.purl`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.purl`|
| [`sbom_urls`](datamodel_attributes.md#sbom)                     | - `$.product_tree.full_product_names[*].product_identification_helper.sbom_urls`<br>- `$.product_tree..branches[*].product.product_identification_helper.sbom_urls`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.sbom_urls` |
| **x\_generic\_uris**            |           |
| [`namespace`](datamodel_attributes.md#x_generic_uris)    | - `$.product_tree.full_product_names[*].product_identification_helper.x_generic_uris[*].namespace`<br>- `$.product_tree..branches[*].product.product_identification_helper.x_generic_uris[*].namespace`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.x_generic_uris[*].namespace`                      |
| [`uri`](datamodel_attributes.md#x_generic_uris)          | *(see above for namespace, replace `namespace` with `uri`)*|
| **Hash**                        |                                                              |
| [`filename`](datamodel_attributes.md#hashes)                      | - `$.product_tree.full_product_names[*].product_identification_helper.hashes[*].filename`<br>- `$.product_tree..branches[*].product.product_identification_helper.hashes[*].filename`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.hashes[*].filename`                                                 |
| **Filehash**                    |                                                                    |
| `algorithm`                     | - `$.product_tree.full_product_names[*].product_identification_helper.hashes[*].file_hashes[*].algorithm`<br>- `$.product_tree..branches[*].product.product_identification_helper.hashes[*].file_hashes[*].algorithm`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.hashes[*].file_hashes[*].algorithm` |
| `value`                         | *(see above, replace `algorithm` with `value`)* |
| **ProductRelationship**         |                                                   |
| `parent`                        | - `($.product_tree.relationships[*].product_reference)` => differenzieren @mrt|
| `type_of_relationship`          | - `$.product_tree.relationships[*].category`|
| `target`                        | - `($.product_tree.relationships[*].relates_to_product_reference)` => differenzieren @mrt|
