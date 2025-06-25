import csv
# create list of dictoinory
employee_data = [
    {"name": "Alice Johnson", "department": "HR", "salary": 55000},
    {"name": "Bob Smith", "department": "Engineering", "salary": 75000},
    {"name": "Charlie Davis", "department": "Marketing", "salary": 62000},
    {"name": "Diana Prince", "department": "Finance", "salary": 70000},
    {"name": "Ethan Brown", "department": "IT", "salary": 68000}
]
# defibne the name of the csv file
csv_file_name = "employees.csv"

# define the field names
fieldnames = ["name", "department", "salary"]
print(f"Attepmpting to write employee data to '{csv_file_name}'.......")

try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        #write the header row
        writer.writeheader()
       # print(f"Successfully wrote {len(employee_data)} ")

       # write all data row
        writer.writerows(employee_data)
    print(f"successfully wrote {len(employee_data)}")

except IOError as e:
    print(f"Error: could not write to file '{csv_file_name}'")