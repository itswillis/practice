# ([4, 3, 2, 1], [1, 1, 1, 1])

# comparasions, swaps

def selection_sort(data):
    compare = 0
    comparasions = [] 
    count = [] 
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        compare += 1
        comparasions.insert(0,compare)
        for i in range(1, pass_num + 1):
            if data[i] > data[position_largest]:
                position_largest = i
        count.append(1)
        data[position_largest], data[i] = data[i], data[position_largest]
    return comparasions, count



numbers = [6, 4]
result = selection_sort(numbers)
print(result)


numbers = [70, 48, 54, 79, 33]
result = selection_sort(numbers)
print(result)