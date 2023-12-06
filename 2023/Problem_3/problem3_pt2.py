# AOC problem 3 part 2

import re

input_file = open("input.txt")
input = input_file.read().splitlines()

# pad input with top row of '...' and front and back columns of '...'
# replace '*' with 'x' so enable regex to work
empty_list = '.' * len(input[0])
input.insert(0, empty_list)
input.append(empty_list)
for i,line in enumerate(input):
    input[i] = '.' + line + '.'
    input[i] = input[i].replace('*','x')

# find 'x' in each line, then determine if a number is adjacent
tally = 0
for i, line in enumerate(input):
    match = re.finditer("x", line)
    for m in match:
        a = []
        m_span = m.span() # start and end index of the value found
        # create string of the characters above, below, front and behind the value
        above = input[i - 1][m_span[0] - 1:m_span[1] + 1]
        below = input[i + 1][m_span[0] - 1:m_span[1] + 1]
        behind = input[i][m_span[0] - 1]
        front = input[i][m_span[1]]

        # create a dictionary mapping change in input index to search location
        s = {above: -1, below: 1, behind: 0, front: 0}

        # For all four search locations
        # use regex to check each searched location for a digit
        for loc in s.keys():
            if re.search(r'\d+', loc):
                # A digit has been found adjacent to the gear
                # the search could have clipped the whole number though
                # get the index locations of all numbers found in the
                # row where the adjacent digit was found
                j = re.finditer(r'\d+', input[i + s[loc]])
                for p in j:
                    pg = int(p.group())
                    ps = p.span()
                    # store numnber if index is adjacent to index of "gear"
                    if (ps[0] <= m_span[1]) and (ps[1] >= m_span[0]):
                        a.append(pg)
                    else:
                        continue
            else:
                continue
        if len(a) > 1:
            tally += (a[0] * a[1])
        else:
            continue

print(tally)