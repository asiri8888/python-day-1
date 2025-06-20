class NegativeNumberError(ValueError):
    """custom exception raised when a negative number is inserted"""
    pass


def get_positive_number():
    """asks the user for a number and raises a NegativeNumberError if"""
    while True:
        try:
            num_str = input("pls enter a positiver number : ")
            number = float(num_str)

            if number < 0:
                raise NegativeNumberError("Number must be positive")
            return number
        except ValueError:
            print("Invlid input. Pls enter a valid number")
        except NegativeNumberError as e:
            print(f"error: {e}")

##below part only run in the file directly and not run in the embeded files
if __name__ == "__main__":
    try:
        positive_num = get_positive_number()
        print(f"You entered a positive number: {positive_num}")
    except NegativeNumberError as e:
        print(f"Caught an error in mai script: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        
