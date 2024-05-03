def get_median_value(numbers):
    numbers = sorted(numbers)
    length = len(numbers)
    median_result = 0

    for _ in range(length):
        if length % 2 != 0:
            median_index = length // 2
            median_result = numbers[median_index]
        else:
            median_index = length // 2
            median_result = (numbers[median_index] + numbers[median_index-1]) / 2
    
    return median_result

print(get_median_value([23, 13, 9, 2]))
print(get_median_value([3, 5, 23, 13, 9]))

    