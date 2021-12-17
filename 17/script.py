file = open("test.txt")

lines = file.readline().strip()

xRange = []
yRange = []

lines = lines.replace('..', '.')
xStr = lines[lines.index('x=')+2:lines.index(',')]
yStr = lines[lines.index('y=')+2:]

xRange = xStr.split('.')
yRange = yStr.split('.')

xRange[:] = [int(meme) for meme in xRange]
yRange[:] = [int(meme) for meme in yRange]

print('part 1:', (-1 * yRange[0] -1) * (-1 * yRange[0]) / 2)