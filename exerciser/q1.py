'''Write a function named modify_list(numbers, value) that takes a list of numbers and a value as parameters. 
The function adds the value to the END of the parameter list. Note: the list is changed in place 
(i.e. the function updates the parameter list and it does not return a new list).'''

def modify_list(numbers, value): 
    numbers.append(value)
    return numbers

source_list1 = [1,2,3]
print("before", source_list1)
modify_list(source_list1, 4)
print("after", source_list1)