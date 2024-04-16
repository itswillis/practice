def get_position_of_largest(data, index):
    largest = 0
    for i in range(1, index+1): # start, stop, step
        if data[i] > data[largest]:
            largest = i
    return largest

def selection_single_pass(data, index):
    largest = get_position_of_largest(data, index)
    data[index], data[largest] = data[largest], data[index]



numbers = [76, 53, 48, 24, 12]
selection_single_pass(numbers, 4)
print(numbers)

numbers = [12, 24, 48, 53, 76]
selection_single_pass(numbers, 3)
print(numbers)