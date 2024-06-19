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
        
    



print(get_selection(0, 5))   

    
