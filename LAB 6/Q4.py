# if there are 5 elements in the list call the selection_single_pass() 5 times


def get_position_of_largest(data, index):
    largest = 0
    for i in range(1, index+1): # start, stop, step
        if data[i] > data[largest]:
            largest = i
    return largest

def selection_single_pass(data, index):
    largest = get_position_of_largest(data, index)
    data[index], data[largest] = data[largest], data[index]

def my_selection_sort(data):
    for index in range(len(data) - 1, 0, -1):
        selection_single_pass(data,index)

numbers = [76, 53, 48, 24, 12]
my_selection_sort(numbers)
print(numbers)
