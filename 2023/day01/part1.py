lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

nums = list(map(lambda n: str(n), range(1, 10)))

def getNum(line):
    line = line.strip()
    n = [0,0]

    for i in range(len(line)):
        if line[i] in nums:
            n[1] = int(line[i])
            if n[0] == 0: n[0] = int(line[i])

    return n[0]*10 + n[1]

print(sum(map(getNum, lines)))