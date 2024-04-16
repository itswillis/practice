# print elements backwards

def print_elements_backward(numbers):
    for i in range(len(numbers) -1, -1, -1):
        print(numbers[i], end=' ')

a_list = [29, 10, 14, 37, 13]
print_elements_backward(a_list)