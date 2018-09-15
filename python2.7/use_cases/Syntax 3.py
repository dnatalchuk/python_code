#!/usr/bin/python

a = 1
b = a
c = b
c = b
c = 1

print id(a)
print id(b)
print id(c)

def f():
	pass
	
	print id(f)
