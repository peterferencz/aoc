lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()
lines[0] = lines[0].strip()

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.arr = [left, right]

dict = {}
for line in lines[2:]:
    a = line.strip().split(' = ')
    b = a[1][1:-1].split(', ')
    node = Node(a[0], b[0], b[1])
    dict[node.name] = node

startingNodes = list(filter(lambda x: x[2] == "A", dict.keys()))
moves = list(map(lambda x: 0 if x == "L" else 1, lines[0]))

def getLoop(startingNode):
    node = startingNode
    visited = {}
    arr = []
    move = 0
    while True:
        if node in visited.keys():
            if move in visited[node]:
                # arr.append(node)
                return [arr, move]
            visited[node].append(move)
        else:
            visited[node] = [move]
        
        arr.append(node)
        node = dict[node].arr[moves[move]]
        move = (move + 1) % len(moves)

startingNodes = list(map(getLoop, startingNodes))
offsets = [0 for i in range(len(startingNodes))]
move = 0
while any(map(lambda x: x[1] > move, startingNodes)): move += 1 # moves to enter each loop

for i in range(len(startingNodes)):
    offsets[i] = move - startingNodes[i][1]
    startingNodes[i] = list(map(lambda x: x[2] == "Z", startingNodes[i][0][startingNodes[i][1]:]))

for i in range(len(startingNodes)):
    print(offsets[i],"".join(['1' if el else '0' for el in startingNodes[i]]))

while True:
    ret = True
    for i in range(len(startingNodes)):
        # print(move, i, startingNodes[i][(move - offsets[i]) % len(startingNodes[i])])
        if not startingNodes[i][(move - offsets[i]) % len(startingNodes[i])]:
            ret = False
    move += 1
    print(move)
    if ret:
        print(move)
        exit(0)