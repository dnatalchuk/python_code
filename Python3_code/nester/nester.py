"""Module for displaying items in nested lists"""

def print_nested_lists(the_list):
        """itteract over the items in lsit, checks type of nested items, iteract and print nested items if any"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_nested_lists(each_item)
        else:
            print(each_item)
