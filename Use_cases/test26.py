#!/usr/bin/python

# ITERABLE object
# list -> items
# dict -> keys
# file -> lines
"""
for i in "denys":
	print i
"""

# ITERATION PROTOCOL
# it takes iterable object and return iterator

# print iter.__doc__

lst = [0,1]
lst = iter(lst)
# next
print next(lst)
print next(lst)
print next(lst)

# GENERATORS
# yield




