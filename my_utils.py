# file_name = 'Agrofood_co2_emission.csv'
# query_column = 0
# query_value = 'Afghanistan'
# result_column = 1 
def get_column(file_name, query_column, query_value, result_column):
    #open file
    f = open(file_name)

    #process line by line
    result_arr = []
    for l in f:
        # turn into array
        arr = l.rstrip().split(',') #really, this is a list
        
        # check to see if the value in the query_column position
        # of the array matches the value
        # stored in the query_value variable
        if arr[query_column]==query_value:
            # append value in result column if true
            result_arr.append(arr[result_column])
    f.close()
    #print(result_arr)
    return result_arr

#get_column(file_name, query_column, query_value, result_column)
