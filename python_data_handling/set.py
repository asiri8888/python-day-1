 # New code for set operations and list de-duplication
print ("----set operations -----")

# create 2 sets
set_a = {10, 20, 30, 40, 50, 50}
set_b = {40, 50, 60, 70, 80}

print(f"set A: {set_a}")
print(f"set B : {set_b}")

# find the union of the set_a abd set_b and print the result
# the union contains all the unique elements of both sets
union_set = set_a.union(set_b)
print(f"union of set_a and set_b is : {union_set}")

# find the intersectiono of set_a and set_b
intersection_set = set_a.intersection(set_b)
print(f"intersection of set_a and setr_b is: {intersection_set}")


# difference set
difference_set = set_a.difference(set_b)
print(f"difference elements of set_a and set_b: {difference_set}")

# create a list with duplicate elements
my_list = [1,2,2,3,4,4,5,4,6,7,7]
print(f"original list with duplicates: {my_list}")

# convet my_list to set to remove duplicates
unique_elements_set = set(my_list)
print(f"list converted to set (remove dupolicates): {unique_elements_set}")


# convet set back to list
# the order of elements might not preserved form the original list