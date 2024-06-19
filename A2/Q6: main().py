def display_intro():
    print("*" * 46)
    print("**        A Number Converter Program        **")
    print("** Decimal --> Binary, Octal or Hexadecimal **")
    print("*" * 46)

def display_menu():
    print("1. Convert to binary value")
    print("2. Convert to octal value")
    print("3. Convert to hexadecimal value")
    print("4. Quit the program")

def get_selection(start, end):
    
    """
    This function prompts the user to make a selection within the range of start and end.
    It keeps prompting the user until a valid integer is entered. 
    "Please make a selection" should only be printed at the start of the function run. 
    Otherwise "Invalid selection" statement should be printed, or a valid value is returned. 

    Authour: William Tang
    """

    selection_input = input("Please make a selection: ")
    while True:
        try: 
            selection_input = int(selection_input)
            if start <= selection_input <= end:
                return selection_input
        except ValueError:
            pass
        selection_input = input("Invalid selection. Try again: ")

def get_number():

    """
    This function prompts the user to enter a positive integer value. The function prompts
    them to try again if the user's input is invalid. The function only considers a
    positive integer is a valid input, and will return it. 

    Authour: William Tang
    """

    input_number = input("Please enter a positive integer: ")
    while True:
        try:
            input_number = int(input_number)
            if input_number > 0:
                return input_number
        except ValueError:
            pass
        input_number = input("Invalid entry. Try again: ")

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

def main():

    '''
    This main program runs the converter program, takes no parameters and should:
    - Display the intro
    - Display the menu
    - Obtains the user selection
    - While the user doesn't select 4:
        - Obtains the decimal value from user
        - Converts this to a value in the selected base and prints out the result of the conversion
        - Displays the menu and reprompts the user to enter their selection. 
    
    Authour: William Tang
    '''

    # display the intro 
    display_intro()
    # display the menu
    display_menu()
    # get the selection number
    print('')
    selection_number = get_selection(1, 4)

    # main function script
    while selection_number != 4:
        if selection_number == 1:
            number = get_number()
            converted_number = convert_number(number, 2)
            print(f"{number} is {converted_number} in binary\n")
        
        elif selection_number == 2:
            number = get_number()
            converted_number = convert_number(number, 8)
            print(f"{number} is {converted_number} in octal\n")

        elif selection_number == 3:
            number = get_number()
            converted_number = convert_number(number, 16)
            print(f"{number} is {converted_number} in hexadecimal\n")
        
        # force re-display menu after conversion
        display_menu()
        print('')
        selection_number = get_selection(1,4)

main()