total_marks=0
for number in range (1,6):
    marks = int(input(f"Pls enter the marks of student {number} : "))   
    total_marks=  total_marks+marks
print(f"the sum of marks of {number} students is : {total_marks}")    
