import copy

file = open("test.txt")
# file = open("test2.txt")
file = open("input.txt")

lines = file.readlines()

class Node:
    connectsWith = []
    name = ""

    def __init__(self, name, connectsWith):
        self.name = name
        self.connectsWith = connectsWith

    def __str__(self) -> str:
        return self.name + str(self.connectsWith)

array = []
for line in lines:
    nope1 = True
    nope2 = True
    line = line.strip()
    parts = line.split('-')
    for i in array:
        if i.name == parts[0]:
            i.connectsWith.append(parts[1])
            nope1 = False
        elif i.name == parts[1]:
            i.connectsWith.append(parts[0])
            nope2 = False
    if nope1:
        array.append(Node(parts[0], [parts[1]]))
    if nope2:
        array.append(Node(parts[1], [parts[0]]))
    
# go through path

def transverseRecursive(currentNode, smallsWent, allWent):
    smallsWentNew = copy.copy(smallsWent)
    allWentNew = copy.copy(allWent)
    if currentNode.name == 'end':
        return 1
    if currentNode.name in smallsWentNew:
        smallsWentNew.append(currentNode.name)
        if currentNode.name[0].islower():
            smallsWentNew.append(currentNode.name)
        return 0
    total = 0
    if currentNode.name[0].islower():
        smallsWentNew.append(currentNode.name)
    allWentNew.append(currentNode.name)
    for i in currentNode.connectsWith:
        nextNode = None
        for v in array:
            if v.name == i:
                nextNode = v
        total += transverseRecursive(nextNode, smallsWentNew, allWentNew)
    return total

start = None
for i in array:
    if i.name == 'start':
        start = i

print('part 1:',transverseRecursive(start, [], []))

def transverseRecursiveP2(currentNode, smallsWent, allWent, twice):
    smallsWentNew = copy.copy(smallsWent)
    allWentNew = copy.copy(allWent)
    if currentNode.name == 'end':
        return 1
    if (currentNode.name in smallsWentNew and twice) or (currentNode.name == 'start' and len(allWent)):
        smallsWentNew.append(currentNode.name)
        if currentNode.name[0].islower():
            smallsWentNew.append(currentNode.name)
        return 0
    elif currentNode.name in smallsWentNew:
        twice = True
    total = 0
    if currentNode.name[0].islower():
        smallsWentNew.append(currentNode.name)
    allWentNew.append(currentNode.name)
    for i in currentNode.connectsWith:
        nextNode = None
        for v in array:
            if v.name == i:
                nextNode = v
        total += transverseRecursiveP2(nextNode, smallsWentNew, allWentNew, twice)
    return total

print('part 2:',transverseRecursiveP2(start, [], [], False))