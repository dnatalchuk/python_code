<<<<<<< HEAD:Condition and control flow 2.py
#!/usr/bin/python

# Conditionals and Control Flow lecture

"""

print 1 == 1

print 50 != (50+1)

bool_answer = 1 == 1
print bool_answer

"""

# if, elif - are related to True value;
# else - related to False

"""

temp = 11

if temp > 11:
	print "temp is %d" %(temp)
	
elif temp == 11:
	print "temp == temp "

else:
	print "None of conditions are true"
	
"""

# OPERATOR IN

"""

var = "alamakota"
if "al" in var:
	print "correct"

else:
	print "is not here"

"""
	
# OPERATOR IS:
# id()

"""

a = 1
b = a

if a is b:
	print id(a), id(b)

else:
	print id(a), id(b)
"""

if type("string") is str:
	print "True"

# 1
num = 4
print "it's 3" if num == 3 else "it's not"

# 2
a = 1
if a == 1: print "1"
elif a == 2: print "2"


=======
#!/usr/bin/python

# Conditionals and Control Flow lecture

"""
In most cases condition "if", "in", "is" is used and boolean values "True" & "False".

if, elif - are related to True value.
else - related to False.
"""

temp = 11

if temp > 11:
	print "temp is %d" %(temp)
	
elif temp == 11:
	print "temp == temp "

else:
	print "None of conditions are true"
	
"""

# OPERATOR IN

"""

var = "alamakota"
if "al" in var:
	print "correct"

else:
	print "is not here"

"""
	
# OPERATOR IS:
# id()

"""

a = 1
b = a

if a is b:
	print id(a), id(b)

else:
	print id(a), id(b)
"""

if type("string") is str:
	print "True"

# 1
num = 4
print "it's 3" if num == 3 else "it's not"

# 2
a = 1
if a == 1: print "1"
elif a == 2: print "2"


>>>>>>> be46e203246a0c7d6b1c6dd632fd6b2be3f6dca4:Conditional_and_control_flow/Condition and control flow 2.py
