import ast
from math import ceil, floor
import copy

file = open("test.txt")
file = open("explodeTest.txt")
file = open("input.txt")
file = open("test3.txt")
# file = open("test2.txt")

lines = file.readlines()

total = 0
totalDep = 0

compArray = []

def applyLeft(array, addValue, sideChaining: list, indice, lastContary):
    if lastContary == None:
        lastContary = ''.join(sideChaining).rindex('R')
    if type(array[1]) == int:
        array[1] += addValue
        return array
    else:
        if indice < lastContary:
            if sideChaining[indice] == 'L':
                return applyLeft(array[0], addValue, sideChaining, indice + 1, lastContary)
            else:
                return applyLeft(array[1], addValue, sideChaining, indice + 1, lastContary)
        elif indice == lastContary:
            return applyLeft(array[0], addValue, sideChaining, indice + 1, lastContary)
        else:
            return applyLeft(array[1], addValue, sideChaining, indice + 1, lastContary)

def applyRight(array, addValue, sideChaining: list, indice, lastContary):
    if lastContary == None:
        lastContary = ''.join(sideChaining).rindex('L')
    if type(array[0]) == int:
        array[0] += addValue
        return array
    else:
        if indice < lastContary:
            if sideChaining[indice] == 'L':
                return applyRight(array[0], addValue, sideChaining, indice + 1, lastContary)
            else:
                return applyRight(array[1], addValue, sideChaining, indice + 1, lastContary)
        elif indice == lastContary:
            return applyRight(array[1], addValue, sideChaining, indice + 1, lastContary)
        else:
            return applyRight(array[0], addValue, sideChaining, indice + 1, lastContary)
        # return applyRight(array[0], addValue, sideChaining, indice + 1,lastContary)

def explode(array):
    left = array[0]
    right = array[1]
    array = 0
    return 0, left, right

def split(array):
    return [floor(array/2), ceil(array/2)]

def simplifyAssignment(array, recursiveDepth, sideChaining: list, arrayBase):
    leftVal = []
    rightVal = []
    sideChainingResult = []

    if recursiveDepth == 4:
        result = explode(array)
        array = result[0]
        left = result[1]
        right = result[2]
        return array, [left], [right], sideChaining
    else:
        if type(array) == list:
            if type(array[0]) == list:
                sideChainingThis = copy.deepcopy(sideChaining)
                sideChainingThis.append('L')
                result = simplifyAssignment(array[0], recursiveDepth + 1, sideChainingThis, arrayBase)
                array[0] = result[0]
                for val in result[1]:
                    leftVal.append(val)
                for val in result[2]:
                    rightVal.append(val)
                if len(rightVal) > 0:
                    if type(array[1]) == int:
                        add = rightVal.pop()
                        array[1] += add
                sideChainingResult = result[3]

            if type(array[1]) == list:
                if len(rightVal) > 0 and len(sideChainingResult) > 0:
                    array[1] = applyRight(array, rightVal.pop(), sideChainingResult, 0, None)

                sideChainingThis = copy.deepcopy(sideChaining)
                sideChainingThis.append('R')
                result = simplifyAssignment(array[1], recursiveDepth + 1, sideChainingThis, arrayBase)
                array[1] = result[0]
                if len(leftVal) > 0:
                    if type(array[0]) == int:
                        add = leftVal.pop()
                        array[0] += add
                for val in result[1]:
                    leftVal.append(val)
                for val in result[2]:
                    rightVal.append(val)
                if len(leftVal) > 0:
                    if type(array[0]) == int:
                        add = leftVal.pop()
                        array[0] += add
                sideChainingResult = result[3]
            
            print(rightVal)
            if type(array[0]) == list:
                if len(leftVal) > 0 and len(sideChaining) == 0 and len(sideChainingResult) > 0:
                    array[0] = applyLeft(array, leftVal.pop(), sideChainingResult, 0, None)

            if type(array[0]) == int and array[0] >= 10:
                array[0] = split(array[0])
                sideChainingThis = copy.deepcopy(sideChaining)
                sideChainingThis.append('L')
                result = simplifyAssignment(array, recursiveDepth, sideChainingThis, arrayBase)
                array = result[0]
                for val in result[1]:
                    leftVal.append(val)
                for val in result[2]:
                    rightVal.append(val)
                sideChainingResult = result[3]

            if type(array[1]) == int and array[1] >= 10:
                array[1] = split(array[1])
                sideChainingThis = copy.deepcopy(sideChaining)
                sideChainingThis.append('R')
                result = simplifyAssignment(array, recursiveDepth, sideChainingThis, arrayBase)
                array = result[0]
                for val in result[1]:
                    leftVal.append(val)
                for val in result[2]:
                    rightVal.append(val)
                sideChainingResult = result[3]

    return array, leftVal, rightVal, sideChainingResult

def addToAssignment(toArray, fromArray):
    if len(toArray) == 0:
        return simplifyAssignment(fromArray, 0, [], fromArray)[0]
    retArray = [copy.deepcopy(toArray), copy.deepcopy(fromArray)]
    # print(retArray)
    retArray = simplifyAssignment(retArray, 0, [], retArray)[0]
    return retArray

for line in lines:
    array = ast.literal_eval(line)
    compArray = addToAssignment(compArray, array)
    print(compArray)

# print(readSnail(compArray,0)[0])
