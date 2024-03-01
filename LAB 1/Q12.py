def create_positive_evens(numbers):
    result = [values for values in numbers if values > 0 and values % 2==0]
    return result

print(create_positive_evens([1, 2, -3, -4, 5, 6, 7, 8, 9, 10, -1, -2]))
print(create_positive_evens([5, 1, -2, 91, 3, -26, -3, -7]))