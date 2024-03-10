# remove all numbers that are positive and odd in the parameter list 
def remove_positive_odds(numbers):
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] >= 0 and numbers[i] % 2 != 0:
            numbers.pop(i)

numbers = [15, 35, 135, 7, -5, 3, -6, 4]
remove_positive_odds(numbers)
print(numbers)