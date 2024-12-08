lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

matrix = []
refMatrix = []
references = {}
numbers = list(map(str, list(range(10))))

def parse():
    useId = 1
    currentid = 0
    for line in lines:
        matrix.append([*line.strip()])
        refMatrix.append([])
        
        for c in line:
            if c in numbers:
                currentid = useId
            elif currentid != 0:
                useId += 1
                currentid = 0
            refMatrix[len(refMatrix)-1].append(currentid)
            if currentid != 0:
                if currentid not in references.keys(): references[currentid] = ""
                references[currentid] += c
    
    for key in references.keys():
        references[key] = int(references[key])
            

# def printMatrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             # print(("\033[94m" if refMatrix[i][j] != 0 else "\033[0m") + matrix[i][j], end='')
#             print(matrix[i][j], end='')
#         print()

parse()

idsToAddUp = 0
# print(len(matrix), len(matrix[0]), matrix[0])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '*': #special char
            thisGear = []
            if i != 0 and j != len(matrix[i])-1: thisGear.append(refMatrix[i-1][j+1]) #tr
            if i != 0: thisGear.append(refMatrix[i-1][j]) #t
            if i != 0 and j != 0: thisGear.append(refMatrix[i-1][j-1]) # tl
            if j != 0: thisGear.append(refMatrix[i][j-1]) # l
            if j != 0 and i != len(matrix)-1: thisGear.append(refMatrix[i+1][j-1]) #bl
            if i != len(matrix)-1: thisGear.append(refMatrix[i+1][j]) # b
            if i != len(matrix)-1 and j != len(matrix[i])-1: thisGear.append(refMatrix[i+1][j+1]) # br
            if j != len(matrix[i])-1: thisGear.append(refMatrix[i][j+1]) #r

            ids = list(map(lambda x: references[x], filter(lambda x: x != 0, set(thisGear))))
            if(len(ids) == 2):
                idsToAddUp += ids[0] * ids[1]


# printMatrix(matrix)
# print('---')
# printMatrix(refMatrix)
# print('---')
print(idsToAddUp)