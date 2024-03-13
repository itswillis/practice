def validate_username(username):
    if not username[:-3].isalpha() or len(username) < 6 or len(username) > 7:
        raise ValueError(f"ERROR: '{username}' - Invalid Format!")

    if not username[-3:].isdigit():
        raise ValueError(f"ERROR: '{username}' - Invalid Format!")

    d1 = int(username[-3])
    d2 = int(username[-2])

    total = d1 * 1 + d2 * 2
    check_digit = total % 9

    if check_digit != int(username[-1]):
        raise ValueError(f"ERROR: '{username}' - Invalid check digit!")

    return check_digit


print(validate_username('acha455'))
print(validate_username('acha568'))
print(validate_username('kng327'))

try:
    print(validate_username('cbur974'))
    print(validate_username('k1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")

try:
    print(validate_username('achang1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")