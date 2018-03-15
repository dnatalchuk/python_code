#!/usr/bin/python
#from __future__ import print_function # import functionality of python higher version

#var = lambda x,y: x+y

#print var(2,3)

# a = lambda s: print(s)
# a("checking")
"""
def f(n):
	
	return lambda x: x + n

print f(2)(3)
"""
"""
lst = ["1","2","3","4"]
int_var = map(int, lst)

print int_var

# map(), filter(), reduce()

print map(float,range(11))

lst = [1,2,3,4]

def f(a):
	print a
map(f,lst)
"""
# FILTER

# filter() -> in Py3 is an iterator

lst = [1,3,9,2,8]
f = lambda a,b: a if(a>b) else b
print reduce(f,lst)
