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
| `model_number (new)`            | - `$.product_tree.full_product_names[*].product_identification_helper.model_numbers[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.model_numbers[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.model_numbers[*]` |
| `Manufacturer:name`             | - `$.product_tree..branches[?(@.category=="vendor")].name`|
| `part_number (article_number)`  | - `$.product_tree.full_product_names[*].product_identification_helper.skus[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.skus[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.skus[*]`|
| `device_family`                 | - `$.product_tree..branches[?(@.category=="product_family")].name`|
| `device_description (new Core)` | - If matching by Full Product Name:<br>- `$.product_tree.full_product_names[*].name`<br>  - `$.product_tree..branches[*].product.name`<br>  - `$.product_tree.relationships[*].full_product_name.name`|
| `cpe`                           | - `$.product_tree.full_product_names[*].product_identification_helper.cpe`<br>- `$.product_tree..branches[*].product.product_identification_helper.cpe`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.cpe`                                        |
| `hardware_version`              | - `$.product_tree..branches[?(@.category=="product_version")].name`<br>- `$.product_tree..branches[?(@.category=="service_pack")].name`<br>- `$.product_tree..branches[?(@.category=="patch_level")].name`<br>- `$.product_tree..branches[?(@.category=="product_version_range")].name`   |
| `hardware_name (new)`           | - `$.product_tree..branches[?(@.category=="product_name")].name`  |
| **Device**                      |   |
| `name`                          | - `$.product_tree..branches[?(@.category=="host_name")].name`  |
| [`serial`](/datamodel_attributes.md#serial-number)                        | - `$.product_tree.full_product_names[*].product_identification_helper.serial_number[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.serial_number[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.serial_number[*]` |
| **Software**                    |   |
| `name`                          | - `$.product_tree..branches[?(@.category=="product_name")].name` |
| `Manufacturer:name`             | - `$.product_tree..branches[?(@.category=="vendor")].name`  |
| `version`                       | - `$.product_tree..branches[?(@.category=="product_version")].name`<br>- `$.product_tree..branches[?(@.category=="service_pack")].name`<br>- `$.product_tree..branches[?(@.category=="patch_level")].name`<br>- `$.product_tree..branches[?(@.category=="product_version_range")].name`                                                         |
| `cpe`                           | *(see above under DeviceType)* |
| `purl`                          | - `$.product_tree.full_product_names[*].product_identification_helper.purl`<br>- `$.product_tree..branches[*].product.product_identification_helper.purl`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.purl`|
| `sbom_urls`                     | - `$.product_tree.full_product_names[*].product_identification_helper.sbom_urls`<br>- `$.product_tree..branches[*].product.product_identification_helper.sbom_urls`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.sbom_urls` |
| **x\_generic\_uris**            |           |
| `namespace`                     | - `$.product_tree.full_product_names[*].product_identification_helper.x_generic_uris[*].namespace`<br>- `$.product_tree..branches[*].product.product_identification_helper.x_generic_uris[*].namespace`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.x_generic_uris[*].namespace`                      |
| `uri`                           | *(see above for namespace, replace `namespace` with `uri`)*|
| **Hash**                        |                                                              |
| `filename`                      | - `$.product_tree.full_product_names[*].product_identification_helper.hashes[*].filename`<br>- `$.product_tree..branches[*].product.product_identification_helper.hashes[*].filename`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.hashes[*].filename`                                                 |
| **Filehash**                    |                                                                    |
| `algorithm`                     | - `$.product_tree.full_product_names[*].product_identification_helper.hashes[*].file_hashes[*].algorithm`<br>- `$.product_tree..branches[*].product.product_identification_helper.hashes[*].file_hashes[*].algorithm`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.hashes[*].file_hashes[*].algorithm` |
| `value`                         | *(see above, replace `algorithm` with `value`)* |
| **ProductRelationship**         |                                                   |
| `parent`                        | - `($.product_tree.relationships[*].product_reference)` => differenzieren @mrt|
| `type_of_relationship`          | - `$.product_tree.relationships[*].category`|
| `target`                        | - `($.product_tree.relationships[*].relates_to_product_reference)` => differenzieren @mrt|
