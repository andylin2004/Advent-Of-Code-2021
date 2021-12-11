file = open("test.txt")
# file = open("test2.txt")
file = open("input.txt")

lines = file.readlines()

fishArray = []
dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,-1,1,1,-1]

totalFlash = 0
stepSync = 0
s = 0

def flashFishRecursive(i,v):
    if fishArray[i][v] > 9:
        total = 1
        fishArray[i][v] = -1
        for x,y in zip(dx,dy):
            if 0 <= i+x < len(fishArray) and 0 <= v+y < len(fishArray[0]) and fishArray[i+x][v+y] != -1:
                fishArray[i+x][v+y] += 1
                total += flashFishRecursive(i+x, v+y, i, v)
        return total
    else:
        return 0

def syncFlash():
    for i in range(len(fishArray)):
        for v in range(len(fishArray[0])):
            if fishArray[i][v] != 0:
                return False

    return True

for line in lines:
    parts = [int(part) for part in line if part != '\n']
    fishArray.append(parts)

while (not syncFlash()):
    s += 1
    for i in range(len(fishArray)):
        for v in range(len(fishArray[0])):
            fishArray[i][v] += 1
    
    for i in range(len(fishArray)):
        for v in range(len(fishArray[0])):
            if s <= 100:
                totalFlash += flashFishRecursive(i,v,-1,-1)
            else:
                flashFishRecursive(i,v,-1,-1)

    for i in range(len(fishArray)):
        for v in range(len(fishArray[0])):
            if fishArray[i][v] == -1:
                fishArray[i][v] = 0

    if (syncFlash()):
        stepSync = s
        break

    print(fishArray)


print(totalFlash)
print(stepSync)