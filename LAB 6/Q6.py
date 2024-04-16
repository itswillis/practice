def my_bubble_sort(data):
    n = len(data)
    for i in range(len(data)):
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1],data[j]
    return data



numbers = [76, 53, 48, 24, 12]
my_bubble_sort(numbers)
print(numbers)