def remove_all_evens(numbers):
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] % 2 == 0: 
            numbers.pop(i)
    return numbers

a_list = [1, 2, 3, 4, 5]
remove_all_evens(a_list)
print(a_list)