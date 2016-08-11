#!/usr/bin/python

"""
=============================================================================================
SCRIPT DESCRIPTION:
=============================================================================================

Idea of this script is get list with randomly generated integer values in range from 0 to 2000, number of values to be generated 
should be passed by user in command line:"./DN_EXAM_SCRIPT.py *number_of values*".

Output will be saved to file "final.txt", at 1st line will be indicated current date and time.

In scope of this script were used:

* importing external modules;
* list;
* class;
* function;
* argv functionality for passing parameters via command line.

Script was created on RHEL 6 OS.
=============================================================================================
"""
# IMPORTING MODULES
 
from datetime import datetime
import random
import sys

# USING CLASS AND FUNCTION

class ExamCl():
	
	def func(): 
		
		date_var = datetime.now()
		d_str = "Current date and time: " + str(date_var) 		# DATE AND TIME VALUE
	
		lst = random.sample(range(0,2001), int(sys.argv[1]))    # GENERATING LIST WITH ARGUMENT TO BE PASSED
		
		my_file = open("final.txt", "w")
		
		for i in d_str: 										# DATE AND TIME VALUE TO BE INDICATED AT 1ST LINE
			my_file.write(str(i))
			
		my_file.write('\n' + '\n')								# ADD EMPTY LINE TO SEPARATE CONTENT
		
		for i in lst: 											# INSERTING GENERATED VALUES TO FILE, SEPARATED BY SPACE
			my_file.write(str(i) + ' ')
			
		my_file.close()
	func()

