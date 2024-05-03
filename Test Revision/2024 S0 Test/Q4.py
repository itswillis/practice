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


'''
def get_list_of_medians(data):
    median_list = []
    for med in data:

        median_result = get_median_value(med)

        median_list.append(median_result)

    return median_list
'''

def get_list_of_medians(data):
    return [get_median_value(med) for med in data]


print(get_list_of_medians([[3, 1, 5, 7], [6, 4, 2]]))
data = [[-9, 3, 4, 6, 2], [33, 52, 3, 14, 63], [3, 5, 4]]
result = get_list_of_medians(data)
print(result)
print(data)