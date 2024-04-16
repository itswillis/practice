def get_position_of_largest(data, index):
    largest = 0
    for i in range(1, index+1): # start, stop, step
        if data[i] > data[largest]:
            largest = i
    return largest



numbers = [20, 27, 69, 10, 76, 41]
print(get_position_of_largest(numbers, 2))