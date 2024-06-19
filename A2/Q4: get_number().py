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

print(get_number())