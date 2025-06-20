try:
    number = int(input("Pls enter an your marks : "))  
    if number>=75:
        print(f"Your grade for {number} marks is A ")
    elif number>=65 :
         print(f"Your grade for {number} marks is  B ")
    elif number>=50 :
         print(f"Your grade for {number} marks is C ")
    elif number>=35:
         print(f"Your grade for {number} marks is  S ")     
    else:
         print(f"Your grade for {number} marks is  F ")  

except ValueError:
    print("Invalid input. please enter whole number")
