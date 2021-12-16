import copy
file = open("test.txt")
file = open("input.txt")

line = file.readline()
line = line.strip()

print(line)

base10 = int(line, 16)
print(base10)
base2 = bin(base10)[2:]
print(base2)
base2N = ''
print(len(base2))
for _ in range(len(base2) % 8, 8):
    if len(base2) % 8 != 0:
        base2N += '0'
base2 = base2N + base2
print(base2)
totalVersion = 0

def subpacket(pointer):
    print('p',pointer)
    pointerOriginal = pointer
    packetVersion = base2[pointer:pointer+3]
    pointer += 3
    packetType = base2[pointer:pointer+3]
    pointer += 3
    meme = base2[pointer:pointer+3]
    print(meme)
    totalLength = 0
    totalSubpackets = 0
    total = 0

    print('type', packetType)
    print('version', packetVersion)
    print('pointer',pointer)

    totalVersion = int(packetVersion, 2)

    if int(packetType, 2) == 4:
        result = ''
        while len(base2) - pointer >= 5:
            print(base2[pointer])
            endAtThis = (int(base2[pointer]) == 0)
            pointer += 1
            print(endAtThis)
            print(pointer)
            bytesRead = base2[pointer:pointer+4]
            result += bytesRead
            pointer += 4
            if endAtThis:
                total = int(result, 2)
                print(result)
                return pointer - pointerOriginal, total, totalVersion
    else:
        if int(base2[pointer]) == 0:
            pointer += 1
            totalBit = base2[pointer:pointer+15]
            totalLength = int(totalBit, 2)
            pointer += 15
            totalBytes = 0
            print(pointer)
            while totalBytes < totalLength:
                result = subpacket(pointer)
                totalBytes += result[0]
                pointer += result[0]
                total += result[1]
                totalVersion += result[2]
                print('e', result[1])
        else:
            pointer += 1
            totalBit = base2[pointer:pointer+11]
            totalSubpackets = int(totalBit, 2)
            pointer += 11
            for _ in range(totalSubpackets):
                result = subpacket(pointer)
                pointer += result[0]
                total += result[1]
                totalVersion += result[2]
                print('a', result[1])

    print(base2)
    return pointer - pointerOriginal, total, totalVersion

result = subpacket(0)

totalVersion = result[2]

print('p1', totalVersion)