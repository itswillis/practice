def rate():
    total = 0
    i = 1
    count = 0 
    inner = 0
    outer = 0
    while i < 2**3:
        j = 0
        outer += 1
        while j < 5:
            total += j 
            j += 2
            inner +=1
        i *= 2
    count = inner + outer
    return (f"Outer: {outer} | Inner: {inner} | Count: {count}")

print(rate())