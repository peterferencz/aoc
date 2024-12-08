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

parse()

idsToAddUp = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] not in numbers and matrix[i][j] != '.': #special char
            if i != 0 and j != len(matrix[i])-1: idsToAddUp.append(refMatrix[i-1][j+1]) #tr
            if i != 0: idsToAddUp.append(refMatrix[i-1][j]) #t
            if i != 0 and j != 0: idsToAddUp.append(refMatrix[i-1][j-1]) # tl
            if j != 0: idsToAddUp.append(refMatrix[i][j-1]) # l
            if j != 0 and i != len(matrix)-1: idsToAddUp.append(refMatrix[i+1][j-1]) #bl
            if i != len(matrix)-1: idsToAddUp.append(refMatrix[i+1][j]) # b
            if i != len(matrix)-1 and j != len(matrix[i])-1: idsToAddUp.append(refMatrix[i+1][j+1]) # br
            if j != len(matrix[i])-1: idsToAddUp.append(refMatrix[i][j+1]) #r


def printMatrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(("\033[94m" if refMatrix[i][j] != 0 else "\033[0m") + matrix[i][j], end='')
        print()

printMatrix()
print('---')
print(sum(map(lambda x: references[x], list(filter(lambda x: x != 0, set(idsToAddUp))))))