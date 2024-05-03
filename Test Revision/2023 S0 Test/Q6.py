def get_word_score(word): 
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'

    lower_str = ''
    for letter in word: 
        letter = letter.lower()
        if letter.isalpha():
            lower_str += letter
            
    score = 0
    for letters in lower_str: 
        if letters in valid_letters:
            # calculate the sum 
            score += valid_letters.index(letters)

    return (lower_str, score)

print(get_word_score('Summer,'))
print(get_word_score('Abd,'))
print(get_word_score('At,'))
print(get_word_score('beat'))
result = get_word_score('beta')
print(type(result))
print(result)
print(get_word_score('AT SCHOOL'))