#!/usr/bin/python

#Displaying time and date

#import time
#print time.ctime()


from datetime import date
"""
#var_time = datetime.now()
#print dir(datetime)
var_today = datetime.today()
print var_today
"""
"""
print var_time

var_year = var_time.year
print var_time.year

print help("string")
"""
# HOME WORK
# check leap year using DATETIME
"""
def leyr(n)
    if datetime.month(2) % 29 == 0
        return TRUE
    
print dir(datetime)
"""

# n = raw_input("Please enter year:") # returns string in output

n = input("Please enter year:") # returns int in output
leyr = (date(n, 3, 1)-date(n, 2, 1)).days
if leyr == 29:
	print n, " - is a leap year."
 
else:
	print n," - isn't a leap."
#print leyr
"""


# Working with module "Calendar"

"""
"""
import calendar
# c = calendar.TextCalendar(calendar.SUNDAY) # displaying calendar in standard/real view;
# c.prmonth(2016, 3) # displaying calendar for March 2016

#print dir(calendar)
#print calendar.isleap(2016)
#print c
"""




