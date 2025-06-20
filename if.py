try:
    number = int(input("Pls enter an integer : "))
    if number>0:
        print(f"The number {number} is positive")
    elif number<0:
        print (f"The number {number} is negative")
    else:
        print(f"The number {number} is zero")

except ValueError:
    print("Invalid input. please enter whole number")