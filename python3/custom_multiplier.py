#!/usr/bin/env python3

class Multiplier:
    """
    Class to manage custom multiplier scope.

    Class with 2 methods implemented.
    The first method consumes an input parameter any non-zero digit (N),
    the second method consumes data from the previous method and based on number N provided, returns a result of multiplication of the last N elements.
    If N=3, the last 3 items are used, so the result of multiplication those last N numbers is returned.
    """
    def __init__(self):
        initial_list = []
        self.initial_list = initial_list

    def add_method(self, N):
        self.N = N
        self.initial_list.append(self.N)

    def multiply(self):
        iter_list = self.initial_list[-self.N:]
        print(iter_list)
        result = 1
        for i in iter_list:
            result = i * result
        print(result)


def main():
    task = Multiplier()

    task.add_method(2)
    task.add_method(3)
    task.add_method(8)
    task.add_method(4)
    task.add_method(2)

    task.multiply()

if __name__ == "__main__":
    main()
