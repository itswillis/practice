def read_fruit_names(filename):
    try:
        input_file = open(filename, 'r')
        contents = input_file.read().split("\n")
        input_file.close()

        lower_case_contents = [fruit.lower() for fruit in contents if fruit]
        return lower_case_contents
        
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []


print(read_fruit_names('fruit_small.txt'))
print(read_fruit_names('input_unknown.txt'))
