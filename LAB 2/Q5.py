#function process_data(continents_data_dict, continent_regions_dict, data_dict):
 #   for each continent in continents_data_dict:
  #      total_arrivals = 0
   #     for each region in continent_regions_dict[continent]:
    #        if region exists in data_dict:
     #           add the value associated with the region to total_arrivals
      #  set continents_data_dict[continent] to a list containing total_arrivals

def process_data(continents_data_dict, continent_regions_dict, data_dict):
    for continent, _ in continents_data_dict.items():
        total_arrivals = []
        sum_total_arrivals = [] 
        grand_total = []
        if continents_data_dict[continent] != []: 
            grand_total = continents_data_dict[continent]
        for country in continent_regions_dict[continent]:
            if country in data_dict.keys():
                total_arrivals.append(data_dict[country])
                sum_total_arrivals = sum(total_arrivals)
        grand_total.append(sum_total_arrivals)              
        continents_data_dict[continent] = grand_total

	
	
continents_dict = {'Europe': [6270], 'America': [11810], 'Oceania': [116490] }
regions_dict = {'Europe': ['UK'], 'America': ['US'], 'Oceania': ['AU', 'FJ', 'CK']}
data_dict = {'AU': 105510, 'US': 17110, 'FJ': 15110, 'UK': 13160, 'CK': 7360}
process_data(continents_dict, regions_dict, data_dict)
for key in sorted(continents_dict):
    print(key, continents_dict[key])