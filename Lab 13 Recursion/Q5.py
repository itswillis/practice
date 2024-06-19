def no_multiples_of_5(numbers):
    if len(numbers) == 0:
        return True
    elif numbers[0] % 5 == 0:
        return False
    else:
        return no_multiples_of_5(numbers[1:])
    
print(no_multiples_of_5([2, 3, 5, 6]))
print(no_multiples_of_5([10, 5, 25, 11, 22]))
print(no_multiples_of_5([]))
print(no_multiples_of_5([3, 6, 9]))