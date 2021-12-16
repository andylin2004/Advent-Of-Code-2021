import copy
file = open("test.txt")
# file = open("input.txt")

line = file.readline()
line = line.strip()

print(line)

base10 = int(line, 16)
print(base10)
base2 = bin(base10)
print(base2)

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

    while pointer < len(base2):
        if int(packetType, 2) == 4:
            print('ye')
            while len(base2) - pointer >= 5:
                pointer += 1
                print(base2[pointer])
                endAtThis = (int(base2[pointer]) == 0)
                print(endAtThis)
                print(pointer)
                bytesRead = base2[pointer:pointer+4]
                print(bytesRead)
                total += int(bytesRead, 2)
                pointer += 4
                if endAtThis:
                    return pointer - pointerOriginal, total
            print('e4', total)
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
                    print('e', result[1])

    return pointer - pointerOriginal, total

print('p1', subpacket(0))