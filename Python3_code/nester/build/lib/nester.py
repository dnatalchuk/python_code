"""Module for displaying items in nested lists"""

def print_nested_lists(the_list, level):
    """Module for displaying items in nested lists"""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_nested_lists(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)