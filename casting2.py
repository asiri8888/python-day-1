favourite_num_str=input("please enter your favourite number")
try:
    converted_num=int(favourite_num_str)
    print(f"\nSuccessfully converted input to an integer: {converted_number}")
    final_result_int=converted_number+10
    print(f"Result after adding 10(integer) : {final_result_int}, Type:{type(final_result_int)}")
expect ValueError:
    print(f"\nInvalid input: '{favourite_num_str}' canot be converted to a number")