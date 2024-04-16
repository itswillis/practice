def shifting(data, index):
    value_to_insert = data[index] # 25 
    current_index = index - 1

    while current_index >= 0 and data[current_index] > value_to_insert:

        data[current_index+1] = data[current_index]
        current_index -= 1
    
    return data


        

numbers = [20, 27, 69, 25, 15, 41]
shifting(numbers, 3)
print(numbers)  # Output: [20, 27, 27, 69, 15, 41]