# AOC problem 2 part 2

import re

input_file = open("input.txt")
input = input_file.read().splitlines()

pattern = r'red|green|blue' # regex pattern
power_sum = 0 # counter for summming ids of possible games

# loop through each game
for game in input:
    game_id = game.split(':')[0].split(' ')[1]
    draws = game.split(':')[1].split(';')

    # counts lists
    red = []
    green = []
    blue = []

    # for each draw of cubes in a game, create a list of colors and a list of counts
    for draw in draws:
        colors = re.findall(pattern, draw) # list of colors found in a single draw
        counts = re.findall(r'\d\d|\d', draw) # list of values found in single draw (double digits, then single digits)

        # for each color found, assign count found at same index to the counts lists
        for i in range(0, len(colors)):
            if colors[i] == 'red':
                red.append(int(counts[i]))
            elif colors[i] == 'green':
                green.append(int(counts[i]))
            elif colors[i] == 'blue':
                blue.append(int(counts[i]))

    # calculate the game "power"
    power = max(red) * max(green) * max(blue)
    power_sum += power

print('power_sum: {}'.format(power_sum))


