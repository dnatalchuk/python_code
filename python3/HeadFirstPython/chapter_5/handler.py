#!/usr/bin/python3
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-';
        (mins,secs) = time_string.split(splitter);
    elif ':' in time_string:
        splitter = ':';
        (mins,secs) = time_string.split(splitter);
    else:
        return(time_string);
    return(mins + '.' + secs);

with open('james.txt') as james:
    jam = james.readline().strip().split(',');
jam1 = [];
for time_string in jam:
    jam1.append(sanitize(time_string));
jam2 = sorted(jam1);
print('Results for James:','\n',(jam2),'\n')

with open('julie.txt') as julie:
    jul = julie.readline().strip().split(',');
jul1 = [];
for time_string in jul:
    jul1.append(sanitize(time_string));
    jul2 = sorted(jul1);
print('Results for Julie','\n',(jul2),'\n')

with open('mikey.txt') as mikey:
    mik = mikey.readline().strip().split(',');
mik1 = [];
for time_string in mik:
    mik1.append(sanitize(time_string));
    mik2 = sorted(mik1);
print('Results for Mikey','\n',(mik2),'\n')

with open('sarah.txt') as sarah:
    sar = sarah.readline().strip().split(',');
sar1 = [];
for time_string in sar:
    sar1.append(sanitize(time_string));
    sar2 = sorted(sar1);
print('Results for Sarah','\n',(sar2))

