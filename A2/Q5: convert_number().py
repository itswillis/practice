def convert_number(number, base):

    """
    This function converts a given positive integer (number) and a base (base).
    This function uses recursion to perform the conversion. 
    It uses a dictionary to store hexadecimal letters from 10-15. The value to 
    its corresponding key (number) will be used as a letter in conversion.
    
    Authour: William Tang
    """

    # base case
    if number == 0:
        return ""
    # recursive case
    algorithm = (number // base)
    converted = (number % base)
    # binary dict for hexadecimal numbers with letters
    if converted > 9:
        hex_letter_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        converted = hex_letter_dict[converted]
    else:
        converted = str(converted)
    return convert_number(algorithm, base) + converted


	
number = 25
base = 2
print(f"{number} in base 10 is {convert_number(number,base)} in base {base}.")