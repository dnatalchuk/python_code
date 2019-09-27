#!/usr/bin/env python3


def fib_num():
    a, b = 0, 1
    for i in range(10):
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    fib_num()
