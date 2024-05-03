def read_fruit_names(filename):
    fruits_list = []
    try:
        file = open(filename, 'r')
        content = file.read().split("\n")

        file.close()

        for fruit in content:
            fruits_list.append(fruit.lower())

        return fruits_list
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []



print(read_fruit_names('fruit_smalls.txt'))