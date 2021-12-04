file = open("input.txt")

lines = file.readlines()

callouts = []
boards = []
boards2 = []
board = []
firstLine = True


def checkBoardForWin(boardIndice):
    for i in range(0, 5):
        for v in range(0, 5):
            if boards[boardIndice][i][v] == 'mark':
                if v == 4:
                    return True
            else:
                break

    for i in range(0, 5):
        for v in range(0, 5):
            if boards[boardIndice][v][i] == 'mark':
                if v == 4:
                    return True
            else:
                break

    return False


def addNums(boardIndice):
    total = 0
    for i in range(0, 5):
        for v in range(0, 5):
            if boards[boardIndice][i][v] != 'mark':
                total += int(boards[boardIndice][i][v])

    return total


for line in lines:
    if firstLine:
        callouts = line.split(',')
    elif line == '\n':
        if len(board) > 0:
            boards.append(board)
            boards2.append(board)
            board = []
    else:
        board.append(line.split())

    firstLine = False

boards.append(board)
boards2.append(board)

def bingo():
    for num in callouts:
        for c in range(0, len(boards)):
            for i in range(0, 5):
                for v in range(0, 5):
                    if num == boards[c][i][v]:
                        boards[c][i][v] = 'mark'
                        if checkBoardForWin(c):
                            print("part 1")
                            print(addNums(c) * int(num))
                            return

bingo()

# p2

def checkBoardForWin2(boardIndice):
    for i in range(0, 5):
        for v in range(0, 5):
            if boards2[boardIndice][i][v] == 'mark':
                if v == 4:
                    return True
            else:
                break

    for i in range(0, 5):
        for v in range(0, 5):
            if boards2[boardIndice][v][i] == 'mark':
                if v == 4:
                    return True
            else:
                break

    return False

def addNums2(boardIndice):
    total = 0
    for i in range(0, 5):
        for v in range(0, 5):
            if boards2[boardIndice][i][v] != 'mark':
                total += int(boards2[boardIndice][i][v])

    return total

def p2():
    c = 0
    for num in callouts:
        # print(num)
        while c < len(boards2):
            for i in range(0, 5):
                for v in range(0, 5):
                    if num == boards2[c][i][v]:
                        boards2[c][i][v] = 'mark'
                        if checkBoardForWin2(c):
                            # print(boards2[c])
                            if len(boards2) == 1:
                                # print(boards2[c])
                                print('part 2')
                                print(addNums2(c) * int(num))
                                # print(addNums2(c))
                                return
                            else:
                                boards2.pop(c)
                                c -= 1
            c += 1
        c = 0

p2()
