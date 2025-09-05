import my_utils
country='United States of America'
country_column = 0 #was "county_column"
fires_column = 2 #choosing savanna fires
# data has more than one fire column: 
#   [savanna, forest, organic soils, humid tropic]-> [2,3, 22, 23]
file_name = 'Agrofood_co2_emission.csv'
fires = my_utils.get_column(file_name =file_name, 
                            query_column =country_column, 
                            query_value = country, 
                            result_column=fires_column)
print(f'Savanna fires in the US: {fires}')
