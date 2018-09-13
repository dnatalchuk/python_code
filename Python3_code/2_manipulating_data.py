#!/usr/bin/python3
import nester

movies = [ "Holy Grail", 1975, "The life of brain", "The meaning of life", ["some movie again", ["sub film1", "sub film2"]]]

nester.print_nested_lists(movies, 0)