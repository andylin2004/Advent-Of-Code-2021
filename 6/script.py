file = open("input.txt")

lines = file.readlines()
from functools import cache


array = []
for line in lines:
    parts = line.split(',')
    for part in parts:
        array.append(int(part))

#p1 bad

# for i in range(0,256):
#     print(i)
#     for v in range(0, len(array)):
#         if array[v] == 0:
#             array[v] = 6
#             array.append(8)
#         else:
#             array[v] -= 1    

# print(len(array))

total = 0

@cache
def recursiveFish(time, days):
    if days <= 0:
        return 1
    elif time == 0:
        return recursiveFish(6, days-1) + recursiveFish(8, days-1)
    else:
        return recursiveFish(0,  days - time)

for num in array:
    total += recursiveFish(num, 80)

print("p1")
print(total)

total = 0

for num in array:
    total += recursiveFish(num, 256)

print("p2")
print(total)