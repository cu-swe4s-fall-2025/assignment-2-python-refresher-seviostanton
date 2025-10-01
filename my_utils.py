def get_column(file_name, query_column, query_value, result_column):
    """
    Return a list of integers from result_column for
    rows where row[query_column] == query_value.

    Args:
        file_name: path to CSV file.
        query_column: index of column to search; ex)
                      column containing country names.
        query_value: value to match for filtering;
                     ex) 'United States of America'
        result_column: index of column to convert elements to int.

    Returns:
        List[int]: values from the specified column.

    Raises:
        ValueError: if conversion to int fails.
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
            try:
                result_arr.append(int(data_arr[result_column]))
            except ValueError:
                raise ValueError(f"Could not convert data in row to int: "
                                 f"{data_arr[result_column]}")

    f.close()
    return result_arr


def _as_int_list(int_arr):
    """
    Convert an iterable of integers to an array of integers.
    Args:
        int_arr: iterable of integers.
    Returns:
        list: list of integers.
    Raises:
        TypeError: if input is not an iterable of integers.
        ValueError: if input is empty.
    """
    try:
        vals = list(int_arr)
    except TypeError:
        raise TypeError("Input must be an iterable of integers.")
    if not vals:
        raise ValueError("Input must be non-empty.")
    if not all(isinstance(v, int) for v in vals):
        raise TypeError("All elements must be integers.")
    return vals


def mean_ints(int_arr):
    """
    Return the mean of a list of numbers.

    Args:
        values: list of numbers.

    Returns:
        float: mean of the list.

    Raises:
        ValueError: if the list is empty.
    """
    int_arr = _as_int_list(int_arr)
    if len(int_arr) == 1:
        return float(int_arr[0])
    if len(int_arr) == 0:
        raise ValueError("Cannot compute mean of empty list.")
    return sum(int_arr) / len(int_arr)


def median_ints(int_arr):
    """
    Return the median of a list of numbers.

    Args:
        values: list of numbers.

    Returns:
        float: median of the list.

    Raises:
        ValueError: if the list is empty.
    """
    int_arr = _as_int_list(int_arr)
    if len(int_arr) == 1:
        return float(int_arr[0])
    if len(int_arr) == 0:
        raise ValueError("Cannot compute median of empty list.")
    int_arr.sort()
    if len(int_arr) % 2 == 1:
        return float(int_arr[len(int_arr) // 2])
    else:
        term_1 = int_arr[len(int_arr) // 2 - 1]
        term_2 = int_arr[len(int_arr) // 2]
        return (term_1 + term_2) / 2.0


def std_ints(int_arr):
    """
    Return the standard deviation of a list of numbers.

    Args:
        values: list of numbers.

    Returns:
        float: standard deviation of the list.

    Raises:
        ValueError: if the list is empty.
    """
    int_arr = _as_int_list(int_arr)
    if len(int_arr) < 2:
        raise ValueError(
            "At least two values are required to"
            " compute standard deviation."
        )
    avg_ints = mean_ints(int_arr)
    variance = sum((x - avg_ints) ** 2 for x in int_arr) / (len(int_arr)-1)
    return variance ** 0.5
