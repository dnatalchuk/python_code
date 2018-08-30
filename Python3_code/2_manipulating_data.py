#!/usr/bin/python3

movies = ["Holy Grail","The life of brain",["The meaning of life", "some movie again",["sub film1", "sub film2"]]]

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for another_item in nested_item:
                    print(another_item);
            else:
                print(nested_item);
    else:
        print(each_item)
