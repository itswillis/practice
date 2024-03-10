def replace_negatives(numbers_list):
    for i in range(len(numbers_list)):
        if numbers_list[i] < 0:
            numbers_list[i] = 0

numbers = [-2, 45.67, 3, 7.29, -8.36, 1034.99]
replace_negatives(numbers)
print(', '.join(["{:.2f}".format(num) for num in numbers]))