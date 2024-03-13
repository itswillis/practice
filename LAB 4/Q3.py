def sum_of_multiples_of_5(numbers, start_index, end_index):

# go from start index to end index: 
    # if the number is a multiple of 5:
        # store number to empty list
    # add all numbers
    a_list = []
    try: 
        for i in range(start_index, end_index+1, 1): 
            if numbers[i] % 5 == 0:
                a_list.append(numbers[i])
    except IndexError: 
        print("ERROR: Out of range!")
        return 0 
    except TypeError:
        print("ERROR: Invalid number!")
        return 0
    else:
        return sum(a_list)

list1 = [1, 5, 9, 2, 8, 5, 10, 6]
print(sum_of_multiples_of_5(list1, 5, 6))

list1 = [5, 2, 15]
print(sum_of_multiples_of_5(list1, 2, 6))

list2 = [1, 'A', 5]
print(sum_of_multiples_of_5(list2, 1, 2))