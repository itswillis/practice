def get_sum_squares(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] * numbers[0] + get_sum_squares(numbers[1:])


numbers = []
print(get_sum_squares(numbers))