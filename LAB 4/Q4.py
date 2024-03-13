def get_building_name(building_dictionary, code):
    try:
        code = int(code)
    except ValueError: 
        print("ERROR: Invalid code!")
        return None 
    except KeyError:
        print("ERROR: Invalid code!")
        return None
    else: 
        if code not in building_dictionary.keys():
            print(f"ERROR: '{code}' is not available.")
            return None
        return building_dictionary[code]


dictionary =  {315: 'Kate Edger Information Commons', 303: 'Science building',
  106: 'Biology Building',206: 'Humanities Building',201: 'Social Sciences Building',110: 'Thomas Building'}

print(get_building_name(dictionary, 123))
print(get_building_name(dictionary, 201))
print(get_building_name(dictionary, '206'))
print(get_building_name(dictionary, 'yes'))