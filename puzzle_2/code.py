###########################################################
with open(r"C:\Ram_local_files\advent_of_code\puzzle_2\input.txt") as f:
    lines = f.read().splitlines()

###########################################################


def isok(values):
    if all(x < y for x, y in zip(values, values[1:])) or all(
        x > y for x, y in zip(values, values[1:])
    ):

        if all(1 <= abs(x - y) <= 3 for x, y in zip(values, values[1:])):
            return 1

    return 0


part1 = 0
part2 = 0

for line in lines:
    values = [int(val) for val in line.split(" ")]

    if isok(values):
        part1 += 1
    else:
        sub_set = [values[:i] + values[i + 1 :] for i in range(len(values))]
        for sub in sub_set:
            if isok(sub):
                part2 += 1
                break


print("part1 = ", part1)
print("part2 = ", part1 + part2)


###########################################################
