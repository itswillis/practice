def bubble_sort(data):
    n = len(data)
    num_comparisons = 0
    num_swaps = 0
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            num_comparisons += 1
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                num_swaps += 1
    return (n, num_comparisons, num_swaps)


