# part 1

input = open("input.txt", "r")

lines = input.readlines()
curNum = -1
increasingNumber = -1

for line in lines:
    if int(line) > curNum:
        increasingNumber += 1
    curNum = int(line)

print("Part 1: ")
print(increasingNumber)

# part 2
increasingNumber = 0
input = open("input.txt", "r")
currentLine = input.readline()
indice = 0
windowArray = [0, 0]
while(currentLine):
    for i in range(indice, indice+2):
        windowArray[i] += int(currentLine)
    windowArray.append(int(currentLine))
    currentLine = input.readline()
    indice += 1

print(windowArray)

for i in range(2, len(windowArray) - 1):
    if windowArray[i + 1] > windowArray[i]:
        print(windowArray[i+1])
        increasingNumber += 1

print("Part 2: ")
print(increasingNumber)