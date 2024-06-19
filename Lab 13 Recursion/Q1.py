def print_lower(word):
    word = word.lower()
    if len(word) == 0:
        print("Go!")
    else:
        print(word[0])
        print_lower(word[1:])


print_lower('ABC')
print_lower('CASE')
