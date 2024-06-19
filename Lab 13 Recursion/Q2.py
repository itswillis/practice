def count_multiples_of_5(numbers):
    if len(numbers) == 0: 
        return 0 
    elif numbers[0] % 5 == 0: 
        return 1 + count_multiples_of_5(numbers[1:])
    else:
        return count_multiples_of_5(numbers[1:])




print(count_multiples_of_5([8, 42, 48, 48, 44, 33, 14, 44, 10, 15, 27, 5, 9, 14, 45, 47, 36, 26, 12]))