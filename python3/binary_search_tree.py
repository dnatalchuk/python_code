#!/usr/bin/env python3


a = [10, 2, 3, 4, 5, 6 , 7, 8, 9, 20]

def BinarySearch(input_list, searched_item):
'''
Function for binary search implementation:
'''
    input_list.sort()
    first_index = 0
    last_index = len(input_list) - 1
    found = False

    while first_index <= last_index and not found:
        midpoint = (first_index + last_index)//2
        if input_list[midpoint] == searched_item:
            found = True
        else:
            if input_list[midpoint] < searched_item:
                first_index = midpoint + 1
            else:
                last_index = midpoint - 1
    if found == False:
        return "Searched item not found in the list!"
    else:
        return "Searched item found and it has index:", input_list.index(searched_item)

result = BinarySearch(a, 10)
