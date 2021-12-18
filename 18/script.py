import ast

file = open("test.txt")
file = open("explodeTest.txt")

lines = file.readlines()

total = 0

def applyLeft(array, addValue):
    print('iybu')
    if type(array[1]) == int:
        array[1] += addValue
    else:
        applyLeft(array[1], addValue)

def applyRight(array, addValue):
    print('ye')
    if type(array[0]) == int:
        array[0] += addValue
    else:
        applyRight(array[0], addValue)

def readSnail(array, recursiveDepth):
    print(recursiveDepth)
    leftVal = None
    rightVal = None
    
    if recursiveDepth == 4:
        leftVal = array[0]
        rightVal = array[1]
        array = 0
        return 0,leftVal,rightVal

    if type(array) == list:
        if type(array[0]) == list:
            print(array[0], 'dn')
            result = readSnail(array[0], recursiveDepth + 1)
            array[0] = result[0]
            print(result[1], result[2])
            if leftVal == None:
                leftVal = result[1]
            if rightVal == None:
                rightVal = result[2]
            if rightVal != None:
                if type(array[1]) == int:
                    array[1] += rightVal
                    rightVal = None
                else:
                    applyRight(array[1], rightVal)
                    rightVal = None
        if type(array[1]) == list:
            print(array[1], 'suey')
            result = readSnail(array[1], recursiveDepth + 1)
            array[1] = result[0]
            print(result[1], result[2])
            if leftVal == None:
                leftVal = result[1]
            if leftVal != None:
                if type(array[0]) == int:
                    array[0] += leftVal
                    leftVal = None
                else:
                    applyLeft(array[0], leftVal)
                    leftVal = None
            if rightVal == None:
                rightVal = result[2]
    
        print(array)
        return abs(int(array[0]))*3 + 2*abs(int(array[1])), leftVal, rightVal
    print(array)
    return array, 0, 0

for line in lines:
    array = ast.literal_eval(line)
    print(readSnail(array, 0)[0], 'ye')
