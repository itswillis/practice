def selection_sort(data):
    length = len(data)
    swaps = 0
    comp = 0 
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        for i in range(1, pass_num + 1):
            comp += 1
            if data[i] > data[position_largest]:
                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]
        swaps += 1
    return (length, comp, swaps)
    

def bubble_sort(data):
    length= len(data)
    swaps = 0
    comp = 0 
    for pass_num in range(len(data)-1, 0, -1):
        for i in range(0, pass_num):
            comp += 1
            if data[i] > data[i+1]:
                swaps += 1
                data[i], data[i+1] = data[i+1], data[i]        
    return (length, comp, swaps)

def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1 #Add 1 to number of comparisons
    return value > item_to_insert

def insertion_sort(data):
    length = len(data)
    comp = 0  
    shifts = 0  
    for index in range(1, len(data)):
        item_to_insert = data[index]
        i = index - 1
        while i >= 0 and data[i] > item_to_insert:
            comp += 1
            data[i + 1] = data[i]
            shifts += 1  
            i -= 1
        if i >= 0:
            comp += 1  # we need to count the comparison that checks and fails the while loop
        data[i + 1] = item_to_insert
    return (length, comp, shifts)

def analysis_sortings(numbers):
    print(f"Numbers: {numbers}")
    print(f"  Sorting| Length| Comparisons| Swaps|")
    print("======================================")

    results_selection = selection_sort(numbers[:])
    print(f"Selection|{results_selection[0]:>7}|{results_selection[1]:>12}|{results_selection[2]:>6}|")

    results_bubble = bubble_sort(numbers[:])
    print(f"   Bubble|{results_bubble[0]:>7}|{results_bubble[1]:>12}|{results_bubble[2]:>6}|")

    results_insertion = insertion_sort(numbers[:])
    print(f"Insertion|{results_insertion[0]:>7}|{results_insertion[1]:>12}|{results_insertion[2]:>6}|")
    



analysis_sortings([3, 1, 5, 7, 6, 4, 2])
