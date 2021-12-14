from collections import Counter

file = open("test.txt")
file = open("input.txt")

lines = file.readlines()

array = []
toEdit = ''
for line in lines:
    if '->' not in line and line != '\n':
        print(line)
        toEdit = line
    elif '->' in line:
        line = line.strip()
        parts = line.split(' ')
        parts[:] = [part for part in parts if part != '->']
        array.append(parts)

toEdit = toEdit.strip()

for w in range(10):
    i = 0
    print(w)
    while i < len(toEdit)-1:
        for v in array:
            if v[0] == toEdit[i:i+2]:
                toEdit = toEdit[:i+1]+v[1]+toEdit[i+1:]

                i += 1
                break
        i += 1

toEdit = toEdit.strip()
mostCommon = Counter(toEdit).most_common()[0]
common  = list(Counter(toEdit).values())
common.sort()
print('part 1:', common[-1] - common[0])

        
