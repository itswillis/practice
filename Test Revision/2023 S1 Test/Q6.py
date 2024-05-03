def collapse(numbers):
    for i in range(len(numbers)):
        if isinstance(numbers[i], list):
            try:
                total = sum(numbers[i])
                numbers[i] = total
            except:
                pass
    return numbers

values = [1.5, ['abc', 1], [2.5, 3]]
collapse(values)
print(values)
