# AOC problem 4 part 1

import re

input_file = open("input.txt")
input = input_file.read().splitlines()

# winning numbers | numbers in the card

total = 0
for r in input:
    x = r.split(':')[1].split('|')
    w = list(filter(None, x[0].split(' ')))
    d = list(filter(None, x[1].split(' ')))
    count = 0
    for i in w:
        if i in d:
            count += 1
    if count > 0:
        total += int(( 2 ** count ) / 2)
print(total)
