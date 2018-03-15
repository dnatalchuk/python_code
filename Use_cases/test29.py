#!/usr/bin/python

# UNDERLINE - some kind of privacy

# __ underline private
"""
class A(object):
	def __test(self):
		print "I am the -test - method in class A"
	def test(self):
		self.__test()

# a = A()
# a.test()

class B(A):
	def __test(self):
		print "I am the -test- method class B"

b = B()
b.test()
"""
		
# FAKE CALCULATOR

number = 10
# 10 + 20

print number.__add__(20)
