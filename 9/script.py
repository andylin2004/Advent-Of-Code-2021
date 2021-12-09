# file = open("test.txt")
file = open("input.txt")

lines = file.readlines()
total = 0

array = []
for line in lines:
    parts = [int(part) for part in line if part != '\n']
    array.append(parts)

isBasinArray = [[0 for i in range(len(array[0]))] for v in range(len(array))]

for i in range(0,len(array)):
    for v in range(0,len(array[0])):
        if i > 0:
            if array[i - 1][v] <= array[i][v]:
                continue
        if i < len(array) - 1:
            if array[i + 1][v] <= array[i][v]:
                continue
        if v > 0:
            if array[i][v - 1] <= array[i][v]:
                continue
        if v < len(array[0]) - 1:
            if array[i][v + 1] <= array[i][v]:
                continue
                
        total += 1 + array[i][v]
        isBasinArray[i][v] = 2

print('part 1: ' + str(total))

for i in range(0,len(array)):
    for v in range(0,len(array[0])):
        if array[i][v] == 9:
            continue
        if isBasinArray[i][v] == 2:
            continue
        if i > 0:
            if array[i - 1][v] < array[i][v]:
                isBasinArray[i][v] = 1
        if i < len(array) - 1:
            if array[i + 1][v] < array[i][v]:
                isBasinArray[i][v] = 1
        if v > 0:
            if array[i][v - 1] < array[i][v]:
                isBasinArray[i][v] = 1
        if v < len(array[0]) - 1:
            if array[i][v + 1] < array[i][v]:
                isBasinArray[i][v] = 1

sizes = []

def getBasinSizeRecur(i, v, prevI, prevV):
    total = 1
    if isBasinArray[i][v] == 0:
        return 0
    isBasinArray[i][v] = 0
    if i > 0:
        if prevI != i - 1:
            total += getBasinSizeRecur(i - 1, v, i, v)
    if i < len(array) - 1:
        if prevI != i + 1:
            total += getBasinSizeRecur(i + 1, v, i, v)
    if v > 0:
        if prevV != v - 1:
            total += getBasinSizeRecur(i, v - 1, i, v)
    if v < len(array[0]) - 1:
        if prevV != v + 1:
            total += getBasinSizeRecur(i, v + 1, i, v)

    return total
            

for i in range(len(array)):
    for v in range(len(array[0])):
        if isBasinArray[i][v] == 2:
            sizes.append(getBasinSizeRecur(i, v, -1, -1))

sizes.sort(reverse=True)

total = sizes[0]
for i in range(1,3):
    total *= sizes[i]

print('part 2: ' + str(total))
                
    