def remove_strings_by_len(words, target_length):
    for letter in reversed(words):
        if len(letter) == target_length:
            words.remove(letter)



words = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(words, 3)
print(words)
