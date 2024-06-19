def get_lucas_count(n):
    if n == 1:
        return (2, 0)
    if n == 2:
        return (1, 0)
    
    previous_1, count_1 = get_lucas_count(n-1)  
    previous_2, count_2 = get_lucas_count(n-2)  
    

    value = previous_1 + previous_2
    

    count = count_1 + count_2 + 2
    
    return (value, count)

data = get_lucas_count(3)
print(type(data))
print(data)
print(get_lucas_count(1))
print(get_lucas_count(2))
