#!/usr/bin/python

import sys

lst = ["a", "a2","233","$$"]

def f(val):
	return [sys.getsizeof(i) for i in val]
print f(lst)

# sort() sorted()

lis = [1,4,3,5]
#lis.sort()

# sorted - do sorting just dynamicaly and values will not be temporary sorted; for sort - it will remain such order

# print sorted(lis)

print "#1", sorted(lst, key=len)
print "#2", sorted(lst,key=f)

# FUNCTION as a LIST element

lst = []
"""
#1

def f1():
	var = "ala"
	return var

# lst.append( f1() )

def f2(x):
	var = "ma kota"
	return var * x
	
new = f2(3)
lst.append(new)

print lst

"""

#3

def f1():
	return "one"
	
def f2():
	return "two"
	
lst = [f1(),f2()]
print lst[0]
