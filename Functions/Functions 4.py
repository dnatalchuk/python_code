#!/usr/bin/python

# BUILT-IN-CONDITIONS

"""
def f(*a):
	print max(a)
	print min(a)
f(-10,-1,100,2,5,99)
"""

"""
def f(b = 3, *args):
	print args
	print b
f(12,33,44)
"""

more = "100"

def my_raise():
	paym = 2000
	more1 = int(more)
	new_paym = paym + more1
	return new_paym
print "My new payment is", my_raise()

"""
def my_raise2():
 print "My new payment is ", my_raise()
my_raise2()
"""
