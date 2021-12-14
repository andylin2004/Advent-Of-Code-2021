import copy

file = open("test.txt")
file = open("input.txt")

lines = file.readlines()

array = []
toEdit = ''
for line in lines:
    if '->' not in line and line != '\n':
        line = line.strip()
        print(line)
        toEdit = line
    elif '->' in line:
        line = line.strip()
        parts = line.split(' ')
        parts[:] = [part for part in parts if part != '->']
        array.append(parts)

toEdit = toEdit.strip()

parts = [] 
chars = []

for i in range(len(toEdit)-1):
    lookingAt = toEdit[i:i+2]
    found = False
    for v in parts:
        if v[0] == toEdit:
            v[1] += 1
            found = True
    if not found:
        inPart = [lookingAt, 1]
        parts.append(inPart)

for i in toEdit:
    found = False
    for v in chars:
        if v[0] == i:
            v[1] += 1
            found = True
    if not found:
        inPart = [i, 1]
        chars.append(inPart)

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

for v in range(40):
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

    if v == 9:
        chars.sort(key=lambda x:x[1])

        print('part 1:', chars[-1][1] - chars[0][1])

chars.sort(key=lambda x:x[1])

print('part 2:', chars[-1][1] - chars[0][1])