# pair up the smallest number in the left list
# with the smallest number in the right list
# then the second smallest with second smallest, and so on
# figure out how far apart the two numbers are
# 3 Add up all the distances

input_file = open("input.txt")
loc = input_file.read().splitlines()
sum = 0
left = []
right = []

for i in loc:
    left.append(int(i.split(' ')[0]))
    right.append(int(i.split(' ')[3]))

left.sort()
right.sort()

for i,x in enumerate(left):
    print(left[i])
    print(right[i])
    sum += abs(left[i] - right[i])

print(sum)
