def insertion_single_pass(data, index):
    value_to_insert = data[index]
    current_index = index - 1
    while current_index >= 0 and data[current_index] > value_to_insert:
        data[current_index + 1] = data[current_index]
        current_index -= 1
    data[current_index + 1] = value_to_insert

def my_insertion_sort(a_list):
    for index in range(1, len(a_list)):
        insertion_single_pass(a_list,index)


numbers = [20, 27, 69, 10, 15, 41]
my_insertion_sort(numbers)
print(numbers)