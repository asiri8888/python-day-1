try:
    numerator_input=input("pls enter the numerator: ")
    numerator=float(numerator_input)

    denominator_input=input("pls enter the denominator : ")
    denominator=float(denominator_input)

    result=numerator/denominator

    print(f"You entered: nnumerator={numerator}, Denominator: {denominator}")
    print(f"The result of the division is : {result}")

except ValueError:
    print("Invalid input. pls enter valid numbers for both numarator and denominator")
except ZeroDivisionError:
    print("cannot devide by zero")

except Exception as e:
    print("An unexpected error occurs")
