file = open("input.txt")

lines = file.readlines()

array = []
arrayd = []


ones = 0
zeros = 0
indice = 0
lineCount = 0
arrayOut = []
arrayOutt = []
result1 = 0
result2 = 0
for line in lines:
    array.append([])
    arrayd.append([])
    lineCount += 1
    for char in line:
        if (char != '\n'):
            array[indice].append(int(char))
            arrayd[indice].append(int(char))
    indice += 1

for j in range(0, 12):
    for i in range(0, lineCount):
        if array[i][j] == 0:
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        arrayOut.append(0)
        arrayOutt.append(1)
    else:
        arrayOut.append(1)
        arrayOutt.append(0)
    ones = 0
    zeros = 0
    
for i in range(0, 12):
    result1 += arrayOut[i] * (2 ** (11 - i))
    result2 += arrayOutt[i] * (2 ** (11 - i))

print("part 1 answer")
print(result1*result2)

# p2

i = 0
lineCountd = lineCount
for j in range(0, 12):
    for i in range(0, lineCount):
        if array[i][j] == 0:
            zeros += 1
        else:
            ones += 1
    i = 0
    if zeros > ones:
        while i<lineCount:
            if array[i][j] == 1:
                array.pop(i)
                lineCount -= 1
            else:
                i += 1
    else:
        while i<lineCount:
            if array[i][j] == 0:
                array.pop(i)
                lineCount -= 1
            else:
                i += 1
    i = 0
    ones = 0
    zeros = 0
    if len(array) == 1:
        break

ones = 0
zeros = 0
       
for j in range(0, 12):
    for i in range(0, lineCountd):
        if arrayd[i][j] == 0:
            zeros += 1
        else:
            ones += 1
    i = 0
    if zeros <= ones:
        while i<lineCountd:
            if arrayd[i][j] == 1:
                arrayd.pop(i)
                lineCountd -= 1
            else:
                i += 1
    else:
        while i<lineCountd:
            if arrayd[i][j] == 0:
                arrayd.pop(i)
                lineCountd -= 1
            else:
                i += 1
    i = 0
    if len(arrayd) == 1:
        break

    ones = 0
    zeros = 0

result1 = 0
result2 = 0

for i in range(0, 12):
    result1 += array[0][i] * (2 ** (11 - i))
    result2 += arrayd[0][i] * (2 ** (11 - i))

print("part 2 answer")
print(result1*result2)