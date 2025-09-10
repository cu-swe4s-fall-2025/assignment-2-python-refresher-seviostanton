# file_name = 'Agrofood_co2_emission.csv'
# query_column = 0
# query_value = 'Afghanistan'
# result_column = 1
def get_column(file_name, query_column, query_value, result_column):
    """Return a list of values from `result_column` for rows where
    `data[query_column] == query_value` in a CSV file.
    """
    # open file
    f = open(file_name)

    # process line by line
    result_arr = []
    for line in f:
        # turn into array
        data_arr = line.rstrip().split(',')  # really, this is a list
        # check to see if the value in the query_column position
        # of the array matches the value
        # stored in the query_value variable
        if data_arr[query_column] == query_value:
            # append value in result column if true
            result_arr.append(data_arr[result_column])
    f.close()
    return result_arr
