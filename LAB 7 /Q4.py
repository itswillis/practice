
# ([4, 3, 2, 1], [1, 0, 0, 0])

def bubble_sort(data):
    comparasions = []
    swaps = [] 
    for pass_num in range(len(data) - 1, 0, -1):
        comparasions_count = 0 
        swaps_count = 0 
        for i in range(0, pass_num):
            comparasions_count += 1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaps_count += 1
        comparasions.append(comparasions_count)
        swaps.append(swaps_count)
    return comparasions, swaps


numbers = [12, 78, 81, 99, 91]
result = bubble_sort(numbers)
print(result)