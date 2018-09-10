"""Module for displaying items in nested lists"""

def print_nested_lists(the_list):
    """Module for displaying items in nested lists"""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_nested_lists(each_item)
        else:
            print(each_item)