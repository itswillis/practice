def rate(n):
    i = 1
    total = 0
    count = 2 + 1
    while i < 8:
        total += i
        i *= 2
        count += 3 
    count +=1 
    print(count)
    return total

rate(5)