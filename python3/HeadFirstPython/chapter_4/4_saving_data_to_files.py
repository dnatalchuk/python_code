#!/usr/bin/python3

import subprocess

try:
    subprocess.run(["rm", "./man.txt"]);
    subprocess.run(["rm", "./other.txt"]);
except:
    pass

try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1);
                line_spoken = line_spoken.strip();
                if role == 'Man':
                    with open("man.txt", "a") as man:
                        print(line_spoken, file=man);
                elif role == 'Other Man':
                    with open("other.txt", "a") as other:
                        print(line_spoken, file=other);
            except ValueError:
                pass
except IOError:
    print('File is missing' + str(err))

print('List for role man is here:', '\n', "./man.txt");
print('\n','List for other role is here:', '\n', "./other.txt");