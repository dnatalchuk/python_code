#!/usr/bin/python3

import subprocess

try:
    subprocess.run(["rm", "./man.txt"]);
    subprocess.run(["rm", "./other.txt"]);
except:
    pass

man = open("man.txt", "a");
other = open("other.txt", "a");

try:
    data = open('sketch.txt');
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1);
            line_spoken = line_spoken.strip();
            if role == 'Man':
                print(line_spoken, file=man);
            elif role == 'Other Man':
                print(line_spoken, file=other);
        except ValueError:
            pass
except IOError:
    print('File is missing')

data.close();
man.close();
other.close();

print('List for role man is here:', '\n', "./man.txt");
#subprocess.run(["cat", "./man.txt"]);

print('\n','List for other role is here:', '\n', "./other.txt");
#subprocess.run(["cat", "./other.txt"]);
#subprocess.run(["rm", "./other.txt"]);