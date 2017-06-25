#!/usr/bin/python3
# Control and output hints

#1
#a = "Kola"; b = "26"; print("His name is {0} and age - {1}".format(a, b)

#2
#a=2; a *= 5; print(a)

#3
#length = 4; wideth = 5; print("Area equals {0} \nPerimetre equals {1}". format(length*wideth, 2*(length+wideth)))

#4
"""
number = 10;
running = True

while running:
    guess = int(input("Enter your digit:"))

    if number == guess:
        print("Hej hej!! You are correct \nBut no prise this time!")
        running = False

    elif number < guess:
        print("Needed digit is less than entered")

    else:print("Needed digit is higher than entered")

else:print("While has finished")

print("Done")
"""

#5
#for i in range(10, 20, 2): print(i)

#6 - functions
#6.1
"""x = 50
def sayhel():
    global x
    print("x =", x)
    x = 10
    print("x new =", x)
sayhel()
print("Outside x =", x) """

#6.2
"""
x = 10
y = 2

def max(x, y):
    #global x
    x = 2
    y = 5

    if x > y:
        print("X is max")
    elif x < y:
        print("Y is max")
    else: print("They're equal!")
max(x, y) """

#6.3
"""def func():
    x = 2
    print("x equals", x)

    def func_nested():
        nonlocal x
        x = 5

    func_nested()
    print("x changed to", x)

func()"""

#6.4
"""
def f(val, pr = 100):
    print("Value in percentage", val/pr)
f(51) """

#6.5
"""
def var(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number

    for key in keywords:
        count += keywords[key]
        return count
print(var(1, 2, 10, 4, etables=20, fruits=10)) """

#7
#name = 'Swaroop'
#if name.startswith('Swa'):
#    print("Yes, it starts with Swa")
set_a = ('val1', 'val2')
set_b = ('key1', 'key2')
#b = a.split(" ")=
#print(b)
#print("-".join(b))

# Class Robot
"""
class Robot:
    population=0

    def __init__(self, name):
        self.name = name
        print('(Initialize {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
#        Dead
        print('{0} destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was the last one'.format(self.name))
        else:
            print('Left {0:d} working robots'.format(Robot.population))

    def sayHi(self):
        print('Hi!my name is {0}'.format(self.name))

    def howmany():
        print('We have {0:d} robots'.format(Robot.population))

    howmany=staticmethod(howmany)

droid1 = Robot('R2 - D2')
droid1.sayHi()
Robot.howmany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howmany()

print("Here they can do some magic")
print("They finished work")

del droid1
del droid2

Robot.howmany()
"""
# OOP chapter
"""
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Created SchoolMember: {0})'.format(self.name))

    def tell(self):

        print('Name: "{0}" Age:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Created teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self,name,age)

        self.marks = marks
        print('(Student created: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks are next:"{0:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()
"""

# Working with Input and Output
"""
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return  text == reverse(text)

something = input('Enter data:')
if (is_palindrome(something)):
    print("This is palindrom")
else:
    print("It is not")
"""
# Writing/reading data from file
"""import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apples','mango','bannana']

f = open(shoplistfile,'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile,'rb')
storedlist = pickle.load(f)

print(storedlist)"""

# Try-except construction

try:
    text = input("Put some data -->")
except EOFError:
    print("Why EOF has been done? ")
except KeyboardInterrupt:
    print("Operation has been canceled")
else:
    print('Entered {0}'.format(text))