def get_check_digit(code):
    return sum(int(code[i]) * i for i in range(len(code))) % 5

print(get_check_digit('013'))
print(get_check_digit('364'))