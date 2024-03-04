# ['Asia:ASIA,IN,ID,CN,TH', 'Europe:UK,EUROPE']
# {'Asia': ['ASIA','IN','ID','CN','TH'], 'Europe': ['UK','EUROPE']}

def create_continent_regions_dictionary(contents):
    a_dict = {}
    for letters in contents:
        x = letters.split(":")
        continent = x[0]
        regions = x[1].split(",")
        if continent not in a_dict:
            a_dict[continent] = []
        a_dict[continent] = regions
    return a_dict


data = ['Europe:UK,EUROPE', 'Asia:ASIA,IN,ID,CN,TH']
a_dict = create_continent_regions_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])