# AOC problem 2 part 1

import re

input_file = open("input.txt")
input = input_file.read().splitlines()

pattern = r'red|green|blue' # regex pattern
sum_ids = 0 # counter for summming ids of possible games

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

    # check if game was possible
    if (max(red) <= 12) and (max(green) <= 13) and (max(blue) <= 14):
        sum_ids += int(game_id)

print('sum_ids: {}'.format(sum_ids))


