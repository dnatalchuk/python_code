#!/usr/bin/python

# raw_input() in Py2 -> returns string value
# input() in Py2 -> returns int value
# input() in Py3 -> return string

"""

def teeth():
	print "Which hand to use to clean my teeth? "
	print "Right or Left?"
	
	hand = raw_input("Type right or left" + "\n")
	hand = hand.lower()
	if hand == "left":
		print "Wow!You are genius"
	if hand == "right":
		print "Nothing changed"
	else:
		print "Please indicate correct value"
		teeth()
		# teeth() - loopping and back to the begginig
		
teeth()

"""

