def linear_search(numbers, target_number):
    count = 0 
    for number in numbers:
        count +=1 
        if number == target_number:
            return (True, count)
    return (False, count)

result = linear_search([54, 26, 93, 17, 77, 20], 32)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
print(type(result))

result = linear_search([93, 54, 78, 18, 61, 13, 36, 42, 16, 60, 58, 92], 61)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))