import math


lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()
toProcess = [1 for _ in range(len(lines))]
toAdd = [0 for _ in range(len(lines))]

for i in range(len(lines)):
    lines[i] = (list(map(lambda x: list(map(int, filter(lambda y: y != "", x.split(' ')))), lines[i].strip().split(': ')[1].split(' | '))))
    lines[i] = len(list(filter(lambda x: x in lines[i][0] , lines[i][1])))

s = 0
while sum(toProcess) != 0:
    for i in range(len(toProcess)):
        if toProcess[i] == 0: continue
        if lines[i] != 0:
            for j in range(1, lines[i]+1):
                toAdd[i+j] += toProcess[i]
        s += toProcess[i]
        toProcess[i] -= toProcess[i]
    toProcess = [sum(x) for x in zip(toProcess, toAdd)]
    toAdd = [0 for _ in range(len(lines))]

print(s)