#!/usr/bin/python
#String formatting

"""
print "I"+"B"+"M"
print "I","B","M"
var = 10
print "How old are you?"
"""
"""
name = "Denys"
surname = "Natalchuk"
print "Hi %s" %name
print "%s %s" %(name,surname)
"""
# formatting string
"""
var = 3.78
print "%d" %(var)
print "%f" %(var)

var_1 = "ala"
print "%r" %(var_1)

val = 123
print repr(val), type(repr(val))
print eval(repr(val)) + 2 # evaluating values
"""

# strip

var = " 00aha10 0 "
print repr(var.strip(" ")) # removing spaces from string
print repr(var.strip(" 01"))
print repr(var.rstrip(" "))
print repr(var.lstrip(" "))

# making reservation

var = "something"
print len(var)

print repr("%11s" %(var))

flo = 4.55

print "%7.3f" %(flo) # it will reserve 7 symbols for displaying and 3 digits after .

inti = 3
print repr("%4d" %(inti))

