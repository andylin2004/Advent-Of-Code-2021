import copy
import functools
import heapq
import sys

file = open("test.txt")
file = open("input.txt")

lines = file.readlines()

dx = [0,1]
dy = [1,0]

array = []
results = []
for line in lines:
    parts = [int(part) for part in line if part != '\n']
    array.append(parts)

@functools.cache
def recursionIn(thisX, thisY, prevX, prevY, total):
    if thisX == len(array) - 1 and thisY == len(array[0]) - 1:
        results.append(total + array[thisX][thisY])
    else:
        for x,y in zip(dx, dy):
            if not (thisX+x == prevX and thisY+y == prevY) and (0 <= thisX+x < len(array) and 0 <= thisY+y < len(array[0])):
                recursionIn(thisX+x, thisY+y, thisX, thisY, total + array[thisX][thisY])

recursionIn(0,0,-1,-1,- array[0][0])
results.sort(reverse=True)

print(results[-1])

array = []

for line in lines:
    parts = []
    for boost in range(5):
        for part in line:
            if part != '\n':
                parts.append((int(part)+boost-1)%9+1)
    array.append(parts)

arrayOne = copy.deepcopy(array)

for boost in range(1,5):
    for line in arrayOne:
        parts = []
        for part in line:
            parts.append((int(part)+boost-1)%9+1)
        array.append(parts)

results = []    

# recursionIn(0,0,-1,-1,-array[0][0])

# results.sort()
# print(results[0])
