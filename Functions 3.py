#!/usr/bin/python

# FUNCTION CALL A FUNCTION

global_var = "- global variable - "

"""
def f():
	local_var = "- local var - "
	print local_var
f()
print local_var
"""

"""
global_var = 1

def f():
		global global_var 
		global_var = 2
f()
print global_var
"""

"""
def test():
	print "test() " , global_var
	
def test2():
	print "test2", test()
# test2()

def test():
	global_var = " - changed global var - "
	return global_var

def test2():
	print test()
test2()

print global_var	
"""
"""
def first_fun(x):
	print "in first fun: ", x
	second_fun(x)
	
def second_fun(y):
	new_y = y * 3
	print "in second_fun: ", new_y
first_fun(5)
"""
"""
def test():
	test_var = "test"
	return test_var

def test2(x = test()):
	print x
test2()
"""

"""
def outer():
	def inner():
		print "inner()"
		def inside_inner():
			print "inside_inner()"
		return inside_inner
	return inner
outer()()()
"""

# print local() - print exisiting local variables

var = 100

def f():
	new_var = var
	new_var += 10
	print locals()
	print new_var
f()

# def number(*args)
