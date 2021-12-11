from statistics import median

file = open("input.txt")

lines = file.readlines()

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']
score = [3, 57, 1197, 25137]

discardTotal = 0
correctionTotals = []

for line in lines:
    lineOpen = []
    correctionTotal = 0
    for char in line:
        if char != '\n' and char in opens:
            lineOpen.append(char)
        elif char != '\n' and char in closes:
            if opens[closes.index(char)] == lineOpen[len(lineOpen) - 1]:
                lineOpen.pop()
            else:
                discardTotal += score[closes.index(char)]
                correctionTotal = -1
                break
    
    if correctionTotal == -1:
        continue
    lineOpen.reverse()
    for char in lineOpen:
        correctionTotal *= 5 
        correctionTotal += opens.index(char) + 1
    
    correctionTotals.append(correctionTotal)

print('part 1: ' + str(discardTotal))

correctionTotals.sort()
print('part 2: ' + str(median(correctionTotals)))