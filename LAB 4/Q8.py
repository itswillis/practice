def read_odds(filename):
    a_list = [] 
    try:
        input_file = open(filename, 'r')
        contents = input_file.read().split()
        input_file.close()
        for number in contents:
            try:
                number = int(number)
                if (number % 2) != 0:
                    a_list.append(number)
            except (TypeError, ValueError):
                pass
        return a_list
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []

print(read_odds("tests.txt"))