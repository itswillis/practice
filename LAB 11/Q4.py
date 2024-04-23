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


def get_list_of_medians(data):
    return [get_median_value(sub_list) for sub_list in data]

    
print(get_list_of_medians([[3, 1, 5, 7], [6, 4, 2]]))
data = [[-9, 3, 4, 6, 2], [33, 52, 3, 14, 63], [3, 5, 4]]
result = get_list_of_medians(data)
print(result)
print(data)
