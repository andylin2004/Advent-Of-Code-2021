from statistics import median, mean
from math import ceil, floor

# file = open("test.txt")
file = open("input.txt")

line = file.readline()

array = []
array = line.split(',')
array[:] = [int(x) for x in array]

median = median(array)

total = 0

array.sort()

total = 0
for x in array:
    if x != median:
        total += abs(median - x)

print("p1")
print(total)

average = floor(mean(array))
average2 = ceil(mean(array))

total = 0
total2 = 0

for x in array:
    total += (abs(average - x )+ 1)*abs(average - x)/2
    total2 += (abs(average2 - x )+ 1)*abs(average2 - x)/2

print("p2")
print(min(total, total2))