#AOC, Day 1, Part 1

#import broken calibration values from the file
input_file = open("input.txt")
broken_calibration_values = input_file.read().splitlines()

# initialize an array that will store the real calibration values
real_calibration_values = []

#iterate through rows of the file
for row in broken_calibration_values:

    # find all numbers in the row
    calibration_numbers = [] # an empty list to store the number(s) found in this row
    for char in row:
        if char.isdigit():
            calibration_numbers.append(int(char))

    # if one 1 number was found, value is that numnber multiplied by 11
    # if more than 1 number was found, take the first one and the second one,
    # the value is ((first_number * 10) + last_number)
    if len(calibration_numbers) == 0:
        calibration_value = calibration_numbers * 11
        real_calibration_values.append(calibration_value)
    else:
        calibration_value = (calibration_numbers[0] * 10) + calibration_numbers[-1]
        real_calibration_values.append(calibration_value)

    print("Row: {}, Numbers: {}, Calibration Value: {}".format(row, calibration_numbers, calibration_value))

answer = sum(real_calibration_values)
print("Answer: {}".format(answer))