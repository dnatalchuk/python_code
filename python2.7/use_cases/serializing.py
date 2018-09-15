#!/usr/bin/python

# SERIALIZING

import marshal

def f():
	return 123
	
var = [[1,2,3,4], "string", 85, True, f()]

data = marshal.dumps(var)

print type(data)
