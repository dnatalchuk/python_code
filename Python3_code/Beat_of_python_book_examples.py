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
def func():
    x = 2
    print("x equals", x)

    def func_nested():
        nonlocal x
        x = 5

    func_nested()
    print("x changed to", x)

func()