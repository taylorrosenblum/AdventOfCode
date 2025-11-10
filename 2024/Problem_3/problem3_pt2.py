import re
input_file = open("input.txt")
input = input_file.read()

pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

tally = 0
enabled = 1

matches = re.finditer(pattern, input)
for match in matches:
    if match.group() == "do()":
        enabled = 1
    elif match.group() == "don't()":
        enabled = 0
    else:
        print(f"MATCH: {match.group()}, {enabled}, {match.group(1)}, {match.group(2)}")
        tally += (int(match.group(1)) * int(match.group(2))) * enabled
        print("_"*5)

print(tally)
