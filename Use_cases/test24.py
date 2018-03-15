#!/usr/bin/python
"""
import sys

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" %i,
		# sys.stdout.flush()
"""
"""
import time

n = 0 
while n < 30:
	print n
	#raw_input("Press Enter")
	time.sleep(4)
	n += 1
"""

# WHILE - ELSE condition
"""
lst = range(1,4)
count = 0

while count < len(lst):
	if lst[count] == 4:
		print "item with index %d is four" %(count)
		break
		count += 1
else:
	print "while is done, condition wasn't met"
	print count
"""

# GAME 1
"""
from random import randint

# a <= N <= b

print "5 number will be genearted"
print "if one of item is 2 - you win"

count = 0
while count < 5:
	num = randint(1,10)
	print "Random number is: " + str(num)
	if num == 2:
		print "You win"
		break
	count += 1
else:
	print "You loose"
"""

# GAME 2
"""
from random import randrange
# randrange(a,b,step)

ran_num = randrange(1,10)

count = 0
while count < 3:
	guess = input("Put your choice: ")
	if guess == ran_num:
		print "You win"
		break
	count += 1
else:
	print "You lose!"
"""
"""
# GAME 3

import random

var = random.choice(range(11))

while True:
	your_choice = input("Put number: ")
	if your_choice > var:
		print "Too large"
		continue
	elif your_choice < var:
		print "Too small"
		continue
	
	print "Congrat, You won!"
	break
"""


