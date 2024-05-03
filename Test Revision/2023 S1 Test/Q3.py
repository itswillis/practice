def get_repeat_dictionary(word):
    repeats_dict = {}
    for char in word: 
        if word.count(char) > 1:
            if char not in repeats_dict:
                repeats_dict[char] = word.count(char)
    return repeats_dict



print(get_repeat_dictionary('hello'))
print(get_repeat_dictionary('bubble'))
print(get_repeat_dictionary('value'))
data = get_repeat_dictionary('statistics')
for key in sorted(data):
    print(key, data[key])