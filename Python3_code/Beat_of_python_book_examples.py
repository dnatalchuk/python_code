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

