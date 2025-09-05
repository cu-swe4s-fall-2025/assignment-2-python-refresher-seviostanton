[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

# Assignment 2: Python Refresher

## Completed Tasks Outline:
1) Completed get_column() in my_utils.py
    - Opens CSV file
    - Loops through rows making a list of each
    - Compares query_column element and query_value combination & stores    desired result_column element value in result_arr and returns the completed list of results.

2) Updated print_fires.py to correctly use get_column() from my_utils.py import
    - There are a total of 4 fire columns in the dataset that can be chosen: [savanna, forest, organic soils, humid tropic] -> [2,3, 22, 23]
    - This implementation selects and prints savanna fires

3) Created a run.sh file that runs print_fires.py