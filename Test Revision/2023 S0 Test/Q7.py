def convert_dictionary(scores_dictionary):
    new_dict = {}

    for key, value in scores_dictionary.items():
        for word in value: 
            length = len(word)
            tup = (word, key)

            if length not in new_dict:
                new_dict[length] = [(word, key)]
            else:
                new_dict[length].append(tup)

    for length in new_dict:
        new_dict[length] = sorted(new_dict[length], key=lambda x: x[0])

    return new_dict

data = {37: ['arcs', 'cars'], 24: ['beat', 'beta'], 53: ['out'], 15: ['can']}
a_dict = convert_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])