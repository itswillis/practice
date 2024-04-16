def bubble_sort(data):
    comparisons = []
    swaps = [] 
    n = len(data)
    comparisons_count = 0 
    swaps_count = 0 
    for pass_num in range(len(data) - 1, 0, -1):
        for i in range(0, pass_num):
            comparisons_count += 1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaps_count += 1
        comparisons.append(comparisons_count)
        swaps.append(swaps_count)
    return n, comparisons_count, swaps_count

def bubble_sort_fast(data):
    n = len(data)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        sorted_flag = True
        for j in range(n - i - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                sorted_flag = False
        if sorted_flag:
            break
    return n, comparisons, swaps


d1 = [12, 15, 19, 37, 39]
result1 = bubble_sort(d1)
print('Normal Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result1[0], result1[1], result1[2]))
d2 = [12, 15, 19, 37, 39]
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))