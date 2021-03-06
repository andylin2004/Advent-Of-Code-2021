import itertools

file = open("input.txt")
# file = open("test.txt")

lines = file.readlines()

dx = [-1, 0, 1]
dy = [-1, 0, 1]

lightIndicator = []
photo = []

for line in lines:
    if len(lightIndicator) == 0:
        line = line.strip()
        lightIndicator[:] = [x for x in line]
    elif line != '\n':
        line = line.strip()
        photoLine = [x for x in line]
        photo.append(photoLine)

for count in range(50):
    for w in photo:
        w.append('.')
        w.insert(0, '.')

    photo.append(['.' for _ in range(len(photo[0]))])
    photo.insert(0, ['.' for _ in range(len(photo[0]))])

    photoNew = [['.' for _ in range(len(photo[0]))] for _ in range(len(photo))]

    for i in range(len(photo)):
        for v in range(len(photo[i])):
            value = ''
            for cx, cy in itertools.product(dx, dy):
                if 0 <= i+cx < len(photo) and 0 <= v+cy < len(photo[0]) and photo[i+cx][v+cy] == '#':
                    value += '1'
                else:
                    value += '0'
            decimalResult = int(value, 2)
            photoNew[i][v] = lightIndicator[decimalResult]
    
    photo = photoNew
    
    if count == 1 or count == 49:
        total = 0
        for line in photo:
            for x in line:
                if x == '#':
                    total += 1
        print(total)