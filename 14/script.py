from collections import Counter
import copy

file = open("test.txt")
file = open("input.txt")

lines = file.readlines()

array = []
toEdit = ''
toEditUnused = ''
for line in lines:
    if '->' not in line and line != '\n':
        line = line.strip()
        print(line)
        toEdit = line
        toEditUnused = toEdit
    elif '->' in line:
        line = line.strip()
        parts = line.split(' ')
        parts[:] = [part for part in parts if part != '->']
        array.append(parts)

toEdit = toEdit.strip()

for _ in range(10):
    i = 0
    while i < len(toEdit)-1:
        for v in array:
            if v[0] == toEdit[i:i+2]:
                toEdit = toEdit[:i+1]+v[1]+toEdit[i+1:]

                i += 1
                break
        i += 1

toEdit = toEdit.strip()
mostCommon = Counter(toEdit).most_common()[0]
common  = list(Counter(toEdit).values())
common.sort()
print('part 1:', common[-1] - common[0])

parts = [] 
chars = []

for i in range(len(toEditUnused)-1):
    lookingAt = toEditUnused[i:i+2]
    found = False
    for v in parts:
        if v[0] == toEditUnused:
            v[1] += 1
            found = True
    if not found:
        inPart = [lookingAt, 1]
        parts.append(inPart)

print(parts)

for i in toEditUnused:
    found = False
    for v in chars:
        if v[0] == i:
            v[1] += 1
            found = True
    if not found:
        inPart = [i, 1]
        chars.append(inPart)

print(chars)

def updateValue(array, name, newVal):
    for i in array:
        if i[0] == name:
            i[1] += newVal
            return
    array.append([name, newVal])
    return

def findIndiceOfName(array, name):
    for i in array:
        if i[0] == name:
            return i[1]

for _ in range(40):
    newParts = copy.deepcopy(parts)
    newChars = copy.deepcopy(chars)

    for i in newParts:
        i[1] = 0

    for i in parts:
        updateValue(newParts, i[0][0]+findIndiceOfName(array, i[0]), i[1])
        updateValue(newParts, findIndiceOfName(array, i[0])+i[0][1], i[1])
        updateValue(newChars, findIndiceOfName(array, i[0]), i[1])
    
    parts = newParts
    chars = newChars

chars.sort(key=lambda x:x[1])

print(chars[-1][1] - chars[0][1])
        
# print(parts)
# print(chars)