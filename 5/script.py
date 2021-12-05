file = open("input.txt")

lines = file.readlines()

points = []
land = []
total = 0

for line in lines:
    parts = line.split()
    coord = []
    print(parts)
    parts[:] = [x for x in parts if x != '->']
    print(parts)
    for part in parts:
        coord.append(part.split(','))
    points.append(coord)
    coord = []

def setupLand():
    for i in range(0, 1000):
        meme = []
        for p in range(0, 1000):
            meme.append(0)
        land.append(meme)
        meme = []

setupLand()

for pair in points:
    if pair[0][0] == pair[1][0]:
        indice1 = min(int(pair[0][1]), int(pair[1][1]))
        indice2 = max(int(pair[0][1]), int(pair[1][1]))
        for i in range(indice1, indice2 + 1):
            land[i][int(pair[0][0])] += 1
    elif pair[0][1] == pair[1][1]:
        indice1 = min(int(pair[0][0]), int(pair[1][0]))
        indice2 = max(int(pair[0][0]), int(pair[1][0]))
        for i in range(indice1, indice2+1):
            land[int(pair[0][1])][i] += 1

def assess(total):
    for i in range(0, 1000):
        for p in range(0, 1000):
            if land[i][p] > 1:
                total += 1

    return total

total = assess(total)

print(total)

# p2

land = []
total = 0

setupLand()

for pair in points:
    if pair[0][0] == pair[1][0]:
        indice1 = min(int(pair[0][1]), int(pair[1][1]))
        indice2 = max(int(pair[0][1]), int(pair[1][1]))
        for i in range(indice1, indice2 + 1):
            land[i][int(pair[0][0])] += 1
    elif pair[0][1] == pair[1][1]:
        indice1 = min(int(pair[0][0]), int(pair[1][0]))
        indice2 = max(int(pair[0][0]), int(pair[1][0]))
        for i in range(indice1, indice2+1):
            land[int(pair[0][1])][i] += 1
    else:
        start = pair[0]
        end = pair[1]
        xChange = 0
        yChange = 0
        y = int(pair[0][0])
        x = int(pair[0][1])
        if int(pair[0][0]) < int(pair[1][0]):
            yChange = 1
        else:
            yChange = -1
            
        if int(pair[0][1]) < int(pair[1][1]):
            xChange = 1
        else:
            xChange = -1
        
        while y != int(pair[1][0]) and x != int(pair[1][1]):
            land[x][y] += 1
            x += xChange
            y += yChange
        
        land[x][y] += 1

total = assess(total)

print(total)