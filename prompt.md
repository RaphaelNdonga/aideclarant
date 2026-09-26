Read all the pdf files under the attachments folder as well as the entry_docs.json document. Each pdf document will be broken down into a  corresponding json object in a new json file using entry_docs.json as the template. Any field that you fail to find should still be included but as a blank string

## 1. commercial_invoice
Get the following details from the commercial_invoice file in the following format:
```json
    "commercial_invoice": {
        "incoterm": "",
        "currency": "",
        "fob_amount": "",
        "freight_amount": "",
        "line_items": [{
            "number": "",
            "name": "",
            "qty": "",
            "unit_price": "",
            "total_price": ""
        }],
        "serial_number": ""
    },
```
### 1. incoterm
- Should be in all capital letters. 

### 2. currency
- Should be the 3 letter acronym of the currency.
- Should be in all capital letters.

### 3. fob_amount
- Should be an integer figure that has been converted to a string.

### 4. freight_amount
- Should be an integer figure that has been converted to a string.

### 5. line_items
Should be an array of items. Each item should be as below:
- number - It should number the product rows sequentially as strings: "1", "2"
- name - For each name, combine its collection or brand name with its product description.
- qty - This is the number of units. Should be an integer figure that has been converted to a string
- unit_price - This is the price of each unit. Should be an integer figure that has been converted to a string
- total_price - This is the total price of all the units combined. Should be an integer figure that has been converted to a string

### 6. serial_number
- This is the unique number that identifies the invoice.

## 2. packing_list
Get the following details from the packing_list file in the following format:

```json
    "packing_list": {
        "line_items": [{
            "number": "",
            "name": "",
            "qty": "",
            "package": {
                "type": "",
                "code": "",
                "qty": ""
            },
            "total_gross_mass": "",
            "total_net_mass": ""
        }],
        "total_containers_x_size": [""]
    }
```
### 1. line_items
Should be an array of items. Each item should be as below:
- number - It should number the product rows sequentially as strings: "1", "2"
- name - For each name, combine its collection or brand name with its product description.
- qty - This is the number of units. Should be an integer figure that has been converted to a string
- package - It will have the "type" of package in full. The "code" of the package will be the abbreviation of the package type in capital letters. If one of the type or code are missing from the packing list, infer from the document: UN-CEFACT-Rec21.xls. The "qty" is the number of packages in the line item.
- total_gross_mass - The total gross mass or total gross weight of the line item.
- total_net_mass - The total net mass or total net weight of the line item

### 2. total_containers_x_size
This is the number of containers x the size of the containers. It is an array.
- Example of format: "2 X 40'HQ" becomes "2x40".

