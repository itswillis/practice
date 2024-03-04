def read_file(filename):
    input_file = open(filename, 'r')
    contents = input_file.read().split("\n")
    input_file.close()

    a_list = []
    for words in contents:
        a_list.append(words)
    return a_list



data = read_file("regions1.txt")
print(data)
print(type(data))
print(type(data[0]))
print(type(data[0][0]), type(data[0][1]), type(data[0][1][0]))

data = read_file("full_names.txt")
print(data)
print(len(data[0]))
print(len(data[1]))
print(len(data[2]))