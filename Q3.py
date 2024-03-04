def create_continents_data_dictionary(a_dict):
    for key, _ in a_dict.items():
        a_dict[key] = []
    return a_dict
    



a_dict = {'Asia': ['ASIA','IN','ID','CN','TH'], 'Europe': ['UK','EUROPE']}
data = create_continents_data_dictionary(a_dict)
for key in sorted(data):
    print(key, data[key])