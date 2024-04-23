import math
def get_median_value(numbers):
    numbers = sorted(numbers)
    length_numbers = len(numbers)

    # if even elements 
    if length_numbers % 2 == 0:
        for _ in range(length_numbers):
            middle = int(length_numbers / 2)
            # middle - 1

            # mid point is sum of index middle and average 2

            middle_1 = int((length_numbers / 2) - 1)

            mid_point = (numbers[middle] + numbers[middle_1])
            
            median = mid_point/2

    else:
        for _ in range(length_numbers):
            mid_point = math.floor(length_numbers/2)

            median = numbers[mid_point]

    return median
            
            
        



numbers = [3, 9, 4]
print(get_median_value(numbers))
print(numbers)
print(get_median_value([13, 10, 9, 3]))
print(get_median_value([13, 10, 9, 3, 4]))
    
print(get_median_value([23, 13, 9, 2]))
print(get_median_value([3, 5, 23, 13, 9]))
