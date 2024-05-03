def remove_strings_by_len(words, target_length):
    for char in reversed(words):
        if len(char) == target_length: 
            words.remove(char)


words = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(words, 3)
print(words)
remove_strings_by_len(words, 4)
print(words)
data = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(data, 7)
print(data)