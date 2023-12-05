# AOC problem 3 part 1

import re

input_file = open("input.txt")
input = input_file.read().splitlines()

# pad input with top row of '...' and front and back columns of '...'
empty_list = '.' * len(input[0])
input.insert(0, empty_list)
input.append(empty_list)
for i,line in enumerate(input):
    input[i] = '.' + line + '.'

# find values in each line, add them to tally if they meet criteria
tally = 0
for i, line in enumerate(input):
    match = re.finditer(r'\d+', line)
    for m in match:
        m_value = m.group() # value found
        m_span = m.span() # start and end index of the value found

        # create string of the characters above, below, front and behind the value
        above = input[i - 1][m_span[0] - 1:m_span[1] + 1]
        below = input[i + 1][m_span[0] - 1:m_span[1] + 1]
        behind = input[i][m_span[0] - 1]
        front = input[i][m_span[1]]

        # combine strings of characters found, and check if string contains more than 1 type of character
        m_adjacent = above + below + front + behind
        if len(set(m_adjacent)) > 1:
            tally += int(m_value)

print(tally)