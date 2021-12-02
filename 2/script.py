file = open("input.txt")
lines = file.readlines()
horiz = 0
dep = 0

for line in lines:
    splitLine = line.split(' ')
    instruction = splitLine[0]
    howMuch = int(splitLine[1])
    if (instruction == "forward"):
        horiz += howMuch
    elif (instruction == "up"):
        dep -= howMuch
    else:
        dep += howMuch
print("Part 1:")
print(horiz*dep)

file = open("input.txt")
lines = file.readlines()

horiz = 0
dep = 0
aim = 0

for line in lines:
    splitLine = line.split(' ')
    instruction = splitLine[0]
    howMuch = int(splitLine[1])
    if (instruction == "forward"):
        horiz += howMuch
        dep += (aim * howMuch)
    elif (instruction == "up"):
        aim -= howMuch
    else:
        aim += howMuch

print("Part 2:")
print(horiz*dep)