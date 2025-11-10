import re
input_file = open("input.txt")
input = input_file.read()
print(input)

pattern = r"mul\((\d+),(\d+)\)"
matches = re.finditer(pattern, input)
tally = 0

for match in matches:
    print(f"MATCH: {match.start()}, {match.group(1)}, {match.group(2)}")
    tally += (int(match.group(1)) * int(match.group(2)))

print(tally)

