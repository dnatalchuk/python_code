#!/usr/bin/python
"""
import os

os.system("dir")

x = os.popen("dir")

print x.read()
"""

# PYTHON EXCEPTIONS

# ASSERTION
"""
def f(n):
	assert(n>10), "no: %d > 10 " %n
	return (n, "yes:")

print f(5)
"""
"""
open("test").read()

# try + except

try:
	open("test").read()
	
except IOError:
	print "ERROR, no file like that"
else:
	print "I opened file"
"""
"""
def f(level):
	if level < 1:
		raise ValueError("Invalid level", level)
f(0)
"""
# INDEX ERROR
"""
import sys

print sys.argv[1]

try:
	if sys.argv[1] == "aix":
		print "aix"
	elif sys.argv[1] == "linux":
		print "linux"
	else:
		print "Not defined!"
		sys.exit("Bye!")
except IndexError:
	print "aix or linux?"
	sys.exit()
"""
