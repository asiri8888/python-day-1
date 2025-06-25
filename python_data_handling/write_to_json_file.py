import json
import datetime
product_data = {
    "products" : [
     {"id": "P001", "name": "Laptop", "Price": 1200, "available": True},
     {"id": "P002", "name": "Smartphone", "Price": 800, "available": False},
     {"id": "P003", "name": "Tablet", "Price": 450, "available": True},
     {"id": "P004", "name": "Monitor", "Price": 300, "available": True},
     {"id": "P005", "name": "Keyboard", "Price": 45, "available": False}
    ],
    "last updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
}

# define the name of the json file
json_file_name = "product.json"
print(f"Attempting to write product data to '{json_file_name}'....")

try:
#open the json fike iun write mode
    with open(json_file_name, mode='w', encoding='utf-8') as json_file
    json.dump(product_data,json_file, indent=4)
    print(f"Scuussfully wrote product data to '{json_file_name}'
          
#except  IOError as e:
#    print(f"Error: Could not write to file '{json_file_name}'.")
