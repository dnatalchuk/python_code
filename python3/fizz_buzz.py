#!/usr/bin/env python3

# n = int(input("Put number to fizzbuzz: "))
def fizz_buzz():
    for n in range(1, 100):
        if n % 3 == 0 and n % 5 == 0:
            print("\nFizzbuzz")
        elif n % 3 == 0:
            print("\nFizz")
        elif n % 5 == 0:
            print("\nBuzz")
        else:
            print("\nNot a fizz_buzz")

fizz_buzz()

if __name__ == "main":
    fizz_buzz()
