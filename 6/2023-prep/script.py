file = open("input.txt")
# file = open("test_input.txt")

input = file.read().split(",")
ages = [0] * 9

print(ages)
for timer in input:
    ages[int(timer)] += 1

for _ in range(256):
    newAges = [0] * 9
    for i in range(1,9):
        newAges[i-1] = ages[i]
    newAges[8] = ages[0]
    newAges[6] += ages[0]

    ages = newAges
    print(ages)

print(sum(ages))