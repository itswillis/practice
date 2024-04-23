def rate():
    total = 0
    i = 1
    inner = 0
    outer = 0
    while i < 2**4:
        outer +=1 
        j = 0
        while j < 2:
            inner +=1 
            total += j 
            j += 2
        i *= 2
    return inner, outer

inner, outer = rate()
print("inner: ", inner, "outer: ", outer)
