def double_evens(numbers_list):
    for i in range(len(numbers_list)):
        if numbers_list[i] % 2 == 0: 
            numbers_list[i] = numbers_list[i] * 2
    return numbers_list


numbers_list = [31, 636, 2042, 40, 447]
print(numbers_list)
double_evens(numbers_list)
print(numbers_list)