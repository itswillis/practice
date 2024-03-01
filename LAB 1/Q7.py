def read_school_census_data(filename):
    input_file = open(filename, 'r')
    contents = input_file.read().split("\n")
    input_file.close()

    # initalise an empty list to store tuples
    a = [] 

    for items in contents:
        values = items.split(",")
        colour = str(values[0])
        height = int(values[1])
        left = int(values[2])
        right = int(values[3])
        t = (colour, height, left, right)
        a.append(t)
    return a 


data = read_school_census_data('data.txt')   
print(data)
print(type(data))
print(type(data[0][0]), type(data[0][1]), type(data[0][2]), type(data[0][3]))