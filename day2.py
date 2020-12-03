import re

with open('inputs/day2.txt') as f:
    lst = f.readlines()

good = 0
for x in lst:
    line = x.split()
    min_let, max_let = map(int, line[0].split('-'))
    letter = line[1][0]
    string = line[2]
    occurences = string.count(letter)
    if min_let <= occurences <= max_let:
        good += 1

print(good)

good = 0
for x in lst:
    line = x.split()
    first_pos, sec_pos = map(int, line[0].split('-'))
    letter = line[1][0]
    string = line[2]
    first = string[first_pos-1] == letter 
    second = string[sec_pos-1] == letter
    if first != second:
        good += 1
print(good)
