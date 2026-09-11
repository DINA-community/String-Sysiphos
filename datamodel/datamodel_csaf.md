# Data model Mapping CSAF

---

[Overview](datamodel.md) | [Attributes](datamodel_attributes.md) | [Roles](datamodel_roles.md) | [Data model Mapping CSAF](datamodel_csaf.md) | [Data model Mapping NetBox](datamodel_netbox.md) | [Data model mapping IDTA](Discussion_datamodel.md)

---

Only relevant attributes for CSAF are shown in the table.

| **ASSET**                       | |
| ------------------------------- | ------------------------------------------------------------------------ |
| **Device/Module Type**                  |  **CSAF (JSON-Path)**|
| [`manufacturer:name`](datamodel_attributes.md#manufacturer-of-device-type)              | - `$.product_tree..branches[?(@.category=="vendor")].name`|
| [`device_family`](datamodel_attributes.md#device-family)                  | - `$.product_tree..branches[?(@.category=="product_family")].name`|
| [`model_number`]((datamodel_attributes.md#model) )            | - `$.product_tree.full_product_names[*].product_identification_helper.model_numbers[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.model_numbers[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.model_numbers[*]` |
| [`part_number`](datamodel_attributes.md#part-number)  | - `$.product_tree.full_product_names[*].product_identification_helper.skus[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.skus[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.skus[*]`|
| [`hardware_version`](datamodel_attributes.md#hardware-version)               | For hardware products <br>- `$.product_tree..branches[?(@.category=="product_version")].name`<br>- `$.product_tree..branches[?(@.category=="service_pack")].name`<br>- `$.product_tree..branches[?(@.category=="patch_level")].name`<br>- `$.product_tree..branches[?(@.category=="product_version_range")].name`   |
| [`hardware_name`](datamodel_attributes.md#hardware-name)           | for hardware products <br>- `$.product_tree..branches[?(@.category=="product_name")].name`  |
| [`device_description`](datamodel_attributes.md#device-description) | - If matching by Full Product Name:<br>- `$.product_tree.full_product_names[*].name`<br>  - `$.product_tree..branches[*].product.name`<br>  - `$.product_tree.relationships[*].full_product_name.name`|
| [`cpe`](datamodel_attributes.md#cpe-software)                             | For hardware products <br>- `$.product_tree.full_product_names[*].product_identification_helper.cpe`<br>- `$.product_tree..branches[*].product.product_identification_helper.cpe`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.cpe`                                        |
| **Device**                      |   |
| [`name`](datamodel_attributes.md#device-name)                            | - `$.product_tree..branches[?(@.category=="host_name")].name`  |
| [`serial`](datamodel_attributes.md#serial-number)                        | - `$.product_tree.full_product_names[*].product_identification_helper.serial_numbers[*]`<br>- `$.product_tree..branches[*].product.product_identification_helper.serial_numbers[*]`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.serial_numbers[*]` |
| **Software**                    |   |
| [`name`](datamodel_attributes.md#software-name)                          | - `$.product_tree..branches[?(@.category=="product_name")].name` |
| [`manufacturer:name`](datamodel_attributes.md#software-manufacturer)    | - `$.product_tree..branches[?(@.category=="vendor")].name`  |
| [`version`](datamodel_attributes.md#software-version)                       | - `$.product_tree..branches[?(@.category=="product_version")].name`<br>- `$.product_tree..branches[?(@.category=="service_pack")].name`<br>- `$.product_tree..branches[?(@.category=="patch_level")].name`<br>- `$.product_tree..branches[?(@.category=="product_version_range")].name`                                                         |
| [`cpe`](datamodel_attributes.md#cpe)                          | For software <br> - `$.product_tree.full_product_names[*].product_identification_helper.cpe`<br>- `$.product_tree..branches[*].product.product_identification_helper.cpe`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.cpe`    |
| [`purl`](datamodel_attributes.md#purl)                         | - `$.product_tree.full_product_names[*].product_identification_helper.purl`<br>- `$.product_tree..branches[*].product.product_identification_helper.purl`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.purl`|
| [`sbom_urls`](datamodel_attributes.md#sbom)                     | - `$.product_tree.full_product_names[*].product_identification_helper.sbom_urls`<br>- `$.product_tree..branches[*].product.product_identification_helper.sbom_urls`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.sbom_urls` |
| **x\_generic\_uris**            |           |
| [`namespace`](datamodel_attributes.md#x_generic_uris)    | - `$.product_tree.full_product_names[*].product_identification_helper.x_generic_uris[*].namespace`<br>- `$.product_tree..branches[*].product.product_identification_helper.x_generic_uris[*].namespace`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.x_generic_uris[*].namespace`                      |
| [`uri`](datamodel_attributes.md#x_generic_uris)          | - `$.product_tree.full_product_names[*].product_identification_helper.x_generic_uris[*].uri`<br>- `$.product_tree..branches[*].product.product_identification_helper.x_generic_uris[*].uri`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.x_generic_uris[*].uri`|
| **Hash**                        |                                                              |
| [`filename`](datamodel_attributes.md#hashes)                      | - `$.product_tree.full_product_names[*].product_identification_helper.hashes[*].filename`<br>- `$.product_tree..branches[*].product.product_identification_helper.hashes[*].filename`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.hashes[*].filename`                                                 |
| **Filehash**                    |                                                                    |
| `algorithm`                     | - `$.product_tree.full_product_names[*].product_identification_helper.hashes[*].file_hashes[*].algorithm`<br>- `$.product_tree..branches[*].product.product_identification_helper.hashes[*].file_hashes[*].algorithm`<br>- `$.product_tree.relationships[*].full_product_name.product_identification_helper.hashes[*].file_hashes[*].algorithm` |
| `value`                         | *(see above, replace `algorithm` with `value`)* |
| **ProductRelationship**         |                                                   |
| `parent`                        | - `&($.product_tree.relationships[*].product_reference)` => Link to product in CSAF file. Value must be de-referenced|
| `type_of_relationship`          | - `$.product_tree.relationships[*].category`|
| `target`                        | - `&($.product_tree.relationships[*].relates_to_product_reference)` => Link to product in CSAF file. Value must be de-referenced|

> Note that with CSAF 2.1 an [Extensions Type Schema](https://docs.oasis-open.org/csaf/csaf/v2.1/schema/extension-content.json) is introduced.

Explanation

| sign  | name              | meaning                                                   | example                       |
|---    |---                |---                                                        |---                            |
|  $    |  root             |  The document root — always the starting point            |  whole CSAF JSON              |
|  ..   |  recursive descent| Look at this node and every node below it, at any depth   |  $..branches                  |
|  [*]  |  wild card        | All elements of an array / all members of an object       |  $.branches[*]                |
|  @    |  current node     | "This node" — the one the filter is testing right now     |  @.category                   |
|  ?()  |  filter expression| Keep only nodes where the test inside is true             | ?(@.category=="product_name") |
