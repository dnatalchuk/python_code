#!/usr/bin/python

# LOGICAL STATEMENTS: AND, NOT, OR

# not - is 1st
# and - is 2nd
# or - is last one
"""
var = "5"
# isdigit - check if value is digit 
print var.isdigit()

val = "string"
# isalpha - check if value is string
print val.isalpha()

var_1 = 4.5
# isinstance() - check if types is correct to indicated
print isinstance(var, float)

# isalnum() - check if all values are numbers

# complex numbers:

print complex(2,3)

c = 2 + 3j
print c.real
print c.imag
"""
"""
import sys
print sys.maxint # check max possible value for int value
print type(sys.maxint+1) # check if value belongs to LONG type
"""
"""

def game():
	
	fav_col = raw_input("what's you favorit color?")
	
	if fav_col != "":
		print "Ok,let's move on"
	else:
		print "please put"
		game()
		
		new_col = "green"
		new_col2 = "blue"
		new_col = new_col.upper()
		
		# first letters:
		
		var = fav_col[0]+new_col[0]+new_col2[0]
		print var
game()
"""

# HOME WORK: 
# 15 
# if num is divided by 3 -> "by 3"
# if num is divided by 5 -> "by 5"
# if num is divided by 15 -> "by 15"
# if num is divided by 3.5.15 -> "python is cool"

def func():
	
	num = input("Please enter value to be divided: ");
	
	if ( num % 3 == 0 and num % 5 == 0 and
	     num % 15 == 0):
			 print "Python is cool!"
	
	elif num % 3 == 0:
		print "Num is divided on 3 easily "
		
	elif num % 5 == 0:
		print "Num is divided on 5 easily "
	
	elif num % 15 == 0:
		print "Num is divided on 15 easily "
		
	else:
		print "Enter normal value."
func()
		   


