#!/usr/bin/python3

data = open('sketch.txt')

def print_file(the_file):
        for each_line in data:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')
print_file(data)
data.close()