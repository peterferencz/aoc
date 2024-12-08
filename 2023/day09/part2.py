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

def findPrevious(line):
    stack = [line]
    while not all(map(lambda x: x == 0, a := getDifferences(stack[-1]))): stack.append(a)
    
    p = 0
    for el in reversed(stack):
        p = el[0] - p
        # print(p, stack[len(stack)-i-1])
    return p
    # return line[0] - sum(list(map(lambda x: -x[0], list(reversed(list(filter(lambda x: x != line, stack)))))))

# print(findPrevious([1,3,6,10,15,21]))

# for line in lines:
#     print(findPrevious(line))

print(sum(list(map(findPrevious, lines))))