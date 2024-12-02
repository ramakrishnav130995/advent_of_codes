###########################################################

left = []
right = []

with open(r"C:\Ram_local_files\advent_of_code\puzzle_1\input.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

left.sort()
right.sort()

###########################################################

distance = []

for x0, y0 in zip(left, right):
    distance.append(abs(y0 - x0))

print(sum(distance))

###########################################################
res = 0

for num in left:
    res += num * right.count(num)

print(res)
