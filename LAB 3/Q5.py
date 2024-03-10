# returns True if there is more than one digit character in the parameter string, False otherwise
def has_more_than_one_digit(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
        if count > 1:
            return True
    return False

print(has_more_than_one_digit('dry'))
print(has_more_than_one_digit('acam023'))
print(has_more_than_one_digit('order'))
print(has_more_than_one_digit('adoulie'))
print(has_more_than_one_digit('oo'))