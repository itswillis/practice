def rate(n):
    total = 0
    i = n
    count = 3
    while i > 1:
        total += i
        i //= 2
        count += 3
    count += 1
    print(f"Number of operations: {count}")
    return total

rate(2)