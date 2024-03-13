# countries: 
'''
US,United States
UK,United Kingdom
CA,Canada
NZ

AU,Australia
'''

def read_countries(filename):
    try:
        input_file = open(filename, 'r')
        contents = input_file.read().split("\n")
        input_file.close()

        result = {}
        for content in contents:
            # skip empty lines
            if content == '':
                continue
            parts = content.split(',')
            try:
                key, value = parts
                result[key] = value
            except ValueError: 
                print(f"ERROR: Invalid '{content}'!")
        return result

    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return {} 





    


print(read_countries('2.txt'))