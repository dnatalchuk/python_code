#!/usr/bin/python
"""
def use_name(new_fun):
	def wrap(name):
		return "your name is " + new_fun(name)
	return wrap

@use_name
def get_name(name):
	return name

print get_name("Denys")
"""
#lgn = use_name(get_name) # decorator

#print lgn("Denys")

def appendBefore(func):
	def wrap():
		return "before " + func()
	return wrap
		
def appendAfter(func):
	def wrap():
		return func() + " after"
	return wrap
		
@appendBefore
@appendAfter

def writeTo():
	return "egg"

print writeTo()
	
# decorator in class

def f_decorator(new_f):
	def wrap(name):
		return "names are: %r" %(new_f(name))
	return wrap
	
class Names(object):
	def __init__(self)
	self.name = "jan"
	self.name2 = "janek"

	@f_decorator
	def get_names(self):
		return self.name + "and " + self.name2
		
print Names().get_names()
