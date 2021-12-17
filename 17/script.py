file = open("test.txt")
file = open("input.txt")

lines = file.readline().strip()

lines = lines.replace('..', '.')
xStr = lines[lines.index('x=')+2:lines.index(',')]
yStr = lines[lines.index('y=')+2:]

xRange = xStr.split('.')
yRange = yStr.split('.')

xRange[:] = [int(meme) for meme in xRange]
yRange[:] = [int(meme) for meme in yRange]

print('part 1:', (-1 * yRange[0] -1) * (-1 * yRange[0]) // 2)

pairSets = []

minXWorkingValue = 0
maxXWorkingValue = xRange[1]
maxYWorkingValue = (-1 * yRange[0] -1)
minYWorkingValue = yRange[0]

while minXWorkingValue * (minXWorkingValue + 1) / 2 < xRange[0]:
    minXWorkingValue += 1

for initDx in range(minXWorkingValue, maxXWorkingValue+1):
    for initDy in range(minYWorkingValue, maxYWorkingValue+1):
        dx = initDx
        dy = initDy
        x = 0
        y = 0
        while x < xRange[0] or y > yRange[1]:
            x += dx
            y += dy
            dy -= 1
            dx = max(0, dx-1)
            if xRange[0] <= x <= xRange[1] and yRange[0] <= y <= yRange[1]:
                pairSets.append((initDx, initDy))
                break
            elif y < yRange[0]:
                break

total = len(set(pairSets))

print('part 2:', total)