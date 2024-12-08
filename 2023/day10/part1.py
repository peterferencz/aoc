lines = []
with open("test.txt", "r") as f:
    lines = f.readlines()

matrix = list(map(lambda x: x.strip(), lines))
UP,DOWN,LEFT,RIGHT = [1, 0], [-1, 0], [0, -1], [0, 1]
dict = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [LEFT, UP],
    "7": [LEFT, DOWN],
    "F": [DOWN, RIGHT],
    ".": []
}

def getStart():
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "S": return [y,x]
    print("No starting position found")
    exit(1)

def getStartPipe():
    y,x = getStart()

    toSearch = []
    if y != 0 and DOWN in dict[matrix[y-1][x]]: toSearch.append(UP)
    if y != len(matrix)-1 and UP in dict[matrix[y+1][x]]: toSearch.append(DOWN)
    if x != len(matrix[y])-1 and LEFT in dict[matrix[y][x+1]]: toSearch.append(RIGHT)
    if x != 0 and RIGHT in dict[matrix[y][x-1]]: toSearch.append(LEFT)
    for key in dict.keys():
        if toSearch[0] in dict[key] and toSearch[1] in dict[key]: return key
    print("couldn't find startpipe type")
    exit(1)

def printMatrix(m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            print(m[y][x], end=" ")
        print()

y,x = getStart()
def getDistanceMatrix():
    ret = [[-1 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    ret[y][x] = 0
    step = 0

    def exploreMoves(moves):
        print("inner", y)
        for m in moves:
            if ret[y+m[0]][x+m[1]] == -1 or ret[y+m[0]][x+m[1]] > step:
                ret[y+m[0]][x+m[1]] = step
                print("inner,inner", y)
                # y += m[0]
        #         x += m[1]
        #         exploreMoves(dict[matrix[y][x]])
        #         y -= m[0]
        #         x -= m[1]
    
    print("outer", y)
    exploreMoves(dict[getStartPipe()])

    return ret



printMatrix(matrix)
print(getStartPipe())
print()
printMatrix(getDistanceMatrix())