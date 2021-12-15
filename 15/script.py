import heapq

file = open("test.txt")
file = open("input.txt")

lines = file.readlines()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

array = []
results = []
for line in lines:
    parts = [int(part) for part in line if part != '\n']
    array.append(parts)

def dij(array):

    # three arrays
    results = [[10000] * len(array[0]) for _ in range(len(array))] # for keeping the least number of steps to get to an array slot
    isVisited = [[False] * len(array[0]) for _ in range(len(array))] # one for keeping track of if we already determined the least number of steps to get to an array slot
    pq = [] # for keeping track of next min slot to go to

    pq.append([0, (0,0)]) # preprocessing start place so we can kickstart checking the neighbors later
    results[0][0] = 0 # preprocessing the start, as it doesn't count at all and we don't want anything bad to happen

    heapq.heapify(pq)

    while len(pq) > 0:
        u = heapq.heappop(pq) # pop out the least first value (the currently lowest num)
        x = u[1][0]
        y = u[1][1]
        if isVisited[x][y]:
            continue
        for cx,cy in zip(dx,dy):
            if 0 <= x+cx < len(array) and 0 <= y+cy < len(array[0]):
                newDist = results[x][y] + array[x+cx][y+cy] # do 
                if results[x+cx][y+cy] > newDist:
                    results[x+cx][y+cy] = newDist
                    heapq.heappush(pq, [newDist, (x+cx, y+cy)])
        
        isVisited[x][y] = True

    return results[-1][-1]

print('part 1:', dij(array))

array = []
arrayOne = []

for line in lines:
    parts = []
    for boost in range(5):
        for part in line:
            if part != '\n':
                parts.append((int(part)+boost-1)%9+1)
    arrayOne.append(parts)

for boost in range(0,5):
    for line in arrayOne:
        parts = []
        for part in line:
            parts.append((int(part)+boost-1)%9+1)
        array.append(parts)

print('part 2:', dij(array))
