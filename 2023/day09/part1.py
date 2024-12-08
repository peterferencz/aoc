lines = []

with open("input.txt", 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = list(map(int, lines[i].strip().split(' ')))


def getDifferences(arr):
    ret = []
    for i in range(len(arr)-1):
        ret.append(arr[i+1] - arr[i])
    return ret

def findNext(line):
    stack = [line]
    while not all(map(lambda x: x == 0, a := getDifferences(stack[-1]))): stack.append(a)
    return sum(list(map(lambda x: x[-1], stack)))

print(sum(list(map(findNext, lines))))