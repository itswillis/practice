def get_valid_input():
    while True:
        number = input(("Enter an odd number between 1 and 100 inclusive: "))
        try: 
            number = int(number)
            if number % 2 != 0 and 1 <= number <= 100:
                return number 
        except ValueError or TypeError:
            pass

print("Valid input: {}".format(get_valid_input()))
