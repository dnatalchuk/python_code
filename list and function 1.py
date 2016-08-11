#!/usr/bin/python

# List and function

lst = [1,2,3]
"""
lst.append(4)
lst.insert(3,"a")
lst.extend('123')

print lst
"""
stri = "juhny" # johny
"""
# print stri.replace("u", "o")
stri = stri[0] + 'o' + stri[2:]
print stri
"""

# tupple 

tup = (1,2,5,6)
tup = tup[:2] + (3,4) + tup[2:]

# print tup

lst = ["a", "b", "c"]

"""
for num, ele in enumerate(lst):
	print num, ele
	if ele == "b":
		lst[num] = "B"
print lst
"""

# remove, pop, del
"""
def f(*i):
	print i
f(1,2,3,4,5,6)
"""
"""
def g(**kwargs):
	print kwargs
g(me='Denys',you = 'who knows')
g(**{'Denys':1,'you':2})

dix = {'Denys':1,'you':2}

def g(a):
	print a
g(dix)


var = "abc_def_123"

a,b,c = var.split("_")

print a,b,c
"""

# unpacking

"""
lst = [1,2,3] # packing
a,b,c = lst # unpacking

lst = [1,2]

def f(a):
	global x,z 
	x, z = lst
	
f(lst)

print x,z
"""
"""
a = "xyzs"
b = "wgys"

for i in a:
	print b.find(i) 
"""

def f(x, y = 3) # x is not defined here 
