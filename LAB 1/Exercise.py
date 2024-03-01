def get_list(numbers):
    ascending = []
    descending = []
    for ascending_num in sorted(numbers):
        ascending.append(ascending_num)
    for descending_num in reversed(ascending):
        descending.append(descending_num)
    return (ascending, descending)

data = [3, 2, 1, 9, 2]
print(get_list(data))
print(data)