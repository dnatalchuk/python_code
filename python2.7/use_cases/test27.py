#!/usr/bin/python
"""
def f(lst):
	count = 0
	while count < len(lst):
		lst[count] *= 2
		count += 1
	yield lst
val = f(lst)
print val

for i in val:
	print i
"""
"""
def f():
	for i in range(5):
		yield i
val = f()

print val
"""

# CLASSES, META-CLASSES
# INITIALIZING
"""
class Work(object):
	status = "new job"
	def __init__(self, name):
		self.name = name

name = "ibm"
my_work = Work(name)
print my_work.name
print my_work.status
"""

"""
var = "ala ma kota"

class Work(object):
	status = "new job"
	number = 111
	def __init__(self, name, years):
		self.name = name
		self.years = years
		print var
		
	def about_work(self):
		return "I work in %s for %d years" %(self.name, self.years)
	
	
	def mod(self):
		self.status = "old job"
		self.number = 222

my_work = Work("ibm",2)		
print my_work.about_work()

print my_work.status
print my_work.number
my_work.mod()
print my_work.status
print my_work.number
"""

"""
val = "123"

class Check(object):
	val = "555"
	def f(self):
		print val
		print self.val
		
Check().f()
"""
"""
# __init__ returns newly created object

class MyClass(object):
	def __init__(self): 		# INITIALIZATION
		return 42
MyClass()
"""

class MyClass(object):
	def __new__(self):
		return 42
	def __init__(self):
		print "never called in this case"
		
print MyClass(), type(MyClass())

class MyClass(object):
	def __new__(self,num):
		self.num = num
		return
