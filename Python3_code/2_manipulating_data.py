#!/usr/bin/python3

movies = ["Holy Grail","The life of brain",["The meaning of life", "some movie again"]]
for each_item in movies:
    if isinstance(each_item, list):
        print(each_item);
    else:
        for nested_item in each_item:
            if isinstance(nested_item, list):
                print(nested_item);
