def consecutive_sum(numbers, target):
    return [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1) if numbers[i] + numbers[i+1] == target]


print(consecutive_sum([3, 2, 1, 4], 5))
print(consecutive_sum([3, 2, 1, 4], 3))
print(consecutive_sum([4, 6, 2, 7, 3, 4], 10))
print(consecutive_sum([4, 6, 2, 7, 3, 4], 9))