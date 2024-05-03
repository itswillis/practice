def print_table(words_list, width):
    for word in words_list: 
        empty_string = ' ' * (width - len(word))
        print(f"|{word}{empty_string}|")

print_table(['Summer', 'is', 'over', 'and', 'the', 'hot', 'days', 'are', 'gone'], 6)