def contains_letter(a_word, a_letter):
    if not a_word:
        return (False, -1)
    if a_word[0] == a_letter:
        return (True, 0)
    rest_search = contains_letter(a_word[1:], a_letter)

    if rest_search[0]:
        return (True, rest_search[1] + 1)

    else:
        return(False, -1)
    
result_test, index = contains_letter("auckland", "d")
print(result_test)
print(index)
