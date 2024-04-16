def bubble_single_pass(data, index):
    for i in range(0, index):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 1)
print(numbers)