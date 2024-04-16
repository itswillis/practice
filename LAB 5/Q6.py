def rate(n):
    total = 0
    i = 0
    count = 3  
    while i < n:
        j = 0
        count += 3 
        while j < n:
            total += j 
            j += 2
            count += 3  
        i += 1
        count += 1  
    count += 1  
    print(f"Number of operations: {count}")
    return total

# Test the function
rate(2)
rate(4)
rate(7)

