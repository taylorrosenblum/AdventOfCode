# figure out exactly how often each number
# from teh left list appears in th right list
# calc similarity score
# multiply each number in the left list by the
# number time it appears in the right list

input_file = open("input.txt")
loc = input_file.read().splitlines()
left = []
right = []
occur = []
similarity = 0

for i in loc:
    left.append(int(i.split(' ')[0]))
    right.append(int(i.split(' ')[3]))

#left.sort()
#right.sort()

for i,x in enumerate(left):
   similarity += x * right.count(x)

print(similarity)