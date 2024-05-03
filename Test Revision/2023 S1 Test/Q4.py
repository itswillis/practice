def create_2d_words_list(word):
    list_2d = []
    for i in range(len(word), 0, -1):
        sub_list = []
        for j in range(1, i+1):
            sub_list.append(word[:j])
        list_2d.append(sub_list)
    return list_2d

print(create_2d_words_list('cat'))






