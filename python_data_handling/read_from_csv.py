import csv

# define the csv file
csv_file_name = "employees.csv"

# define the depatment to filter
target_department = "IT"
print(f"attempting to read from the file '{csv_file_name}")
filtered_employees = []

try:
    #open the csv file in read mode
    with open(csv_file_name, mode='r', newline='') as csv_file:
    # create a csv.DictReader object
    # this reader will treat each row a a dictionary using the heade rrow
        reader = csv.DictReader(csv_file)
        for row in reader:
    #check if the 'Department' of current row matche witht the 
            if row.get('department') == target_department:
             filtered_employees.append(row)
    print(f"Filtered employee list : {filtered_employees}")
    
except FileNotFoundError:
    print(f"error: the file '{csv_file_name}' was not found")
except Exception as e:
    print(f"an unexpected error occured: {e}")