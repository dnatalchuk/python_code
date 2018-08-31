#!/usr/bin/python3

movies = ["Holy Grail","The life of brain",["The meaning of life", "some movie again",["sub film1", "sub film2"]]]

# for each_item in movies:
#     if isinstance(each_item, list):
#         for nested_item in each_item:
#             if isinstance(nested_item, list):
#                 for another_item in nested_item:
#                     print(another_item);
#             else:
#                 print(nested_item);
#     else:
#         print(each_item)

# put repeatble code above into a reusable function
def print_nested_lists(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_nested_lists(each_item)
        else:
            print(each_item)

print_nested_lists(movies)
