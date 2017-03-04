#!/usr/bin/python

"""
lst = ["ala", "123"]

for i in lst:
	if i.isalpha() is True:
		print i
		break
else:
	print "isn't alpha"
"""
	
# JUST ZIP
"""
lst_a = range(10)
lst_b = range(11,14) # ZIP is taking the shortest list
lst_c = range(16,22)

print zip(lst_a, lst_b, lst_c, "str")
"""
"""
# ZIP to create new objects/variables

for x,y in zip(["a", "b", "c"], [1,2,3]):
	globals()[x] = y
	
print a
print b
print c
"""
