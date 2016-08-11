#!/usr/bin/python
"""
class Parent(object):
	var = 10
	def __init__(self):
		print "calling parent constructor"
		
	def parentMethod(self):
		print "calling parent method"
		
	def setAttr(slef,attr):
		self.var = attr
		
	def getAttr(self):
		print "Parent attribute", self.var
		
class Child(object):
	def __init__(self):
		print "calling child constructor"
	
	def childMethod(self):
		print "calling child method"
	
c = Child()
c.childMethod()
c.parentMethod()
"""

# SUPER CLASS

"""
class A(object):
	
	def method(self):
		print "# class A"
		return "I"
		
	def method_one(self,arg):
		self.arg = arg
		return "I don't"
		
class B(A):
	def method(self):
		print "# class B"
		return super(B, self).method() + " like Python"
	def method_one(self, arg):
		print "# class B"
		return super(B, self).method_one(arg) + ""
		
z = B()
print z.method()
"""

