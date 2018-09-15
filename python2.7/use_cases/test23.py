#!/usr/bin/python

# WHILE
"""
while True:
	print "True"
	break
	
# if string and numbers - True, but 0 - False1
"""
"""
num = 0
if num <= 0:
	print "it is"

while num < 10:
	print num
	num += 1
"""
"""
import sys

count = 0
while True:
	print count
	count += 1
	var = 555
	if count >= 10:
		break
		s#ys.exit("finished") # sys.exit - will break code and next commands will not be completed
		
print count
print var
"""
choice = raw_input("Do you like ice cream? y/n  :")
while choice != "y" and choice != "n":
	choice = raw_input("Can't be like that  ")
