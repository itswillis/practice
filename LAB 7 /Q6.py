def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1 #Add 1 to number of comparisons
    return value > item_to_insert

def insertion_sort(a_list):
    comparisons = []
    shifts = []
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1
        comparison_count = [0]
        shift_count = 0 
        while i >= 0 and compare(a_list[i], item_to_insert, comparison_count):
            a_list[i + 1] = a_list[i]
            i -= 1
            shift_count += 1
        a_list[i + 1] = item_to_insert
        comparisons.append(comparison_count[0])
        shifts.append(shift_count)
    return comparisons, shifts


numbers = [50, 63, 11, 79, 22, 70, 65, 39, 97, 48]
result = insertion_sort(numbers)
print(result)

numbers = [92, 86, 77, 66, 51, 42, 33, 23]
result = insertion_sort(numbers)
print(result)