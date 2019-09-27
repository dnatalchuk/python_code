#!/usr/bin/env python3


class Goodone:
    def __init__(self, name, surn):
        self.name = name
        self.surn = surn

    def greet(self):
        print("Hi dear {} {}".format(self.name, self.surn))


def main():
    sam = Goodone("Good", "Sir")
    sam.greet()

    test = Goodone("test1", "test2")
    test.greet()


if __name__ == "__main__":
    main()
