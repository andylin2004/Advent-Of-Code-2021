file = open("input.txt")
# file = open("test.txt")
# file = open("3test.txt")
# file = open("2test.txt")

lines = file.readlines()

array = []
for line in lines:
    inOutPair = []
    parts = line.split('|')
    inOutPair.append(parts[0].split())
    inOutPair.append(parts[1].split())
    array.append(inOutPair)

total = 0
for part in array:
    for out in part[1]:
        if len(out) == 2 or len(out) == 4 or len(out) == 7 or len(out) == 3:
            total += 1

print("part 1: " + str(total))

total = 0

for part in array:
    top = ''
    topL = ''
    topR = ''
    middle = ''
    bottomL = ''
    bottomR = ''
    bottom = ''
    organizedArray = ['']*10
    for out in part[0]:
        if len(out) == 2:
            organizedArray[1] = out
        elif len(out) == 7:
            organizedArray[8] = out
        elif len(out) == 3:
            organizedArray[7] = out
        elif len(out) == 4:
            organizedArray[4] = out

    # find what makes top lit
    split1 = organizedArray[7]
    split2 = organizedArray[1]
    top = list(set(split1).difference(split2))[0]

    for out in part[0]:
        # find what makes top right lit and 6
        if len(out) == 6 and len(list(set(out).intersection(organizedArray[7]))) == 2 and len(list(set(out).intersection(organizedArray[8]))) == 6:
            organizedArray[6] = out
            topR = list(set(organizedArray[8]).difference(out))[0]

    for out in part[0]:
        #find what 5 is and the top right area
        if len(out) == 5 and len(list(set(organizedArray[6]).intersection(out))) == 5:
            organizedArray[5] = out
            bottomL = list(set(organizedArray[6]).difference(organizedArray[5]))[0]
    
    for out in part[0]:
        #find what 0 is and middle area
        if len(out) == 6 and len(list(set(organizedArray[6]).intersection(out))) == 5 and bottomL in out:
            organizedArray[0] = out
            middle = list(set(organizedArray[8]).difference(out))[0]

    for out in part[0]:
        #find what 9 is
        if len(out) == 6 and list(set(organizedArray[8]).difference(out))[0] == bottomL:
            organizedArray[9] = out
        #find what 8 is and bottom
        elif len(out) == 5 and len(list(set(out).difference({top, topR, middle, bottomL}))) == 1:
            bottom = list(set(out).difference({top, topR, middle, bottomL}))[0]
            organizedArray[2] = out

    # process of elimination: we can find what 3 is
    organizedArray[3] = list(set(part[0]).difference(organizedArray))[0]

    result = ''
    for out in part[1]:
        i = 0
        while i<10:
            if len(list(set(organizedArray[i]).difference(out))) == 0 and len(organizedArray[i]) == len(out):
                result += str(i)
                break
            i += 1

    total += int(result)

print("part 2: " + str(total))