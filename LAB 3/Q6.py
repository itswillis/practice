def get_median_value(numbers):
    new = []
    for num in numbers:
        new.append(num)
    new.sort()
    if len(new) % 2 != 0: #odd number of elements
        return new[len(new)//2]
    mid_index = len(new)//2
    return (new[mid_index-1] + new[mid_index]) / 2

numbers = [3, 9, 4]
print(get_median_value(numbers))
print(numbers)
print(get_median_value([13, 10, 9, 3]))
print(get_median_value([13, 10, 9, 3, 4]))
