#AOC, Day 1, Part 2

import re

#import broken calibration values from the file
input_file = open("input.txt")
broken_calibration_values = input_file.read().splitlines()
#broken_calibration_values = ['onexxxoneight']

# word numbers
word_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))' # that little ?=( fucker took me 2 hours

# initialize an array that will store the real calibration values
real_calibration_values = []

#iterate through rows of the file
for row in broken_calibration_values:

    # find all integers and words like one, two, three...
    match = re.findall(pattern, row.lower())
    ints = match[:]

    # convert all matches to integers, if word use dictionary, else just convert str to int
    for i, value in enumerate(ints):
        if value in word_num.keys():
            ints[i] = word_num[value]
        else:
            ints[i] = int(ints[i])

    # if one 1 number was found, value is that numnber multiplied by 11
    # if more than 1 number was found, take the first one and the second one,
    # the value is ((first_number * 10) + last_number)
    if len(ints) == 0:
        calibration_value = ints * 11
        real_calibration_values.append(calibration_value)
    else:
        calibration_value = (ints[0] * 10) + ints[-1]
        real_calibration_values.append(calibration_value)

    print("row: {}, match: {}, ints {}, value: {}".format(row, match, ints, calibration_value))

answer = sum(real_calibration_values)
print("Answer: {}".format(answer))
