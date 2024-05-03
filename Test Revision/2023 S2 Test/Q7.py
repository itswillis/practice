def validate(nhi_number):
    letters = nhi_number[:3]
    digits = nhi_number[4:]

    if len(nhi_number) != 7:
        raise ValueError(f"ERROR: '{nhi_number}' - Invalid length!")
    
    if not letters.isalpha() or len(letters) != 3: 
        raise ValueError(f"ERROR: '{nhi_number}' - does not start with 3 alphabetical letters!")
    
    if not digits.isdigit() or len(digits) != 4: 
        raise ValueError(f"ERROR: '{nhi_number}' - does not end with 4 digits!")

    return (letters, int(digits))
    

try:
    print(validate('ab12345'))
except ValueError as e:
    print(e)
else:
    print("Well done!")