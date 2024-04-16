def linear_search_sorted(numbers, target_number):
    count = 0 
    for number in numbers:
        count +=1 
        if number == target_number:
            return (True, count)
        elif number > target_number:
            return (False, count)
    return (False, count)

result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 6)
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))

result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 4)
print(type(result))
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))
