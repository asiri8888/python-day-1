# represent the list in a dictionoary
# each disctionaly item reprent the product keys like id, name, price and stock
inventory = [
    {"id": "P001", "name": "Laptop", "Price": 1200, "Stock": 50},
    {"id": "P002", "name": "Smartphone", "Price": 800, "Stock": 120},
    {"id": "P003", "name": "Tablet", "Price": 450, "Stock": 75},
    {"id": "P004", "name": "Monitor", "Price": 300, "Stock": 40},
    {"id": "P005", "name": "Keyboard", "Price": 45, "Stock": 150}
]

print ("-------print initial inventory-------")
# Print table header
print(f"{'ID':<6} {'Name':<15} {'Price ($)':<10} {'Stock':<6}")
print("-" * 40)

# Print each product in a formatted row
for p in inventory:
    print(f"{p['id']:<6} {p['name']:<15} {p['Price']:<10} {p['Stock']:<6}")

