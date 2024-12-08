lines = []
with open("input.txt", "r") as f:
    lines = list(map(lambda x: list(map(int, x.strip().split())), f.readlines()))

def isSafeDamp(line):
    print(line)
    for j in range(len(line)):
        l = line[:j] + line[j+1:]
        print("  " + str(l))
        if isSafe(l):
            return True
    return False

def isSafe(line):
    asc = line[0] < line[1]
    for i in range(len(line) -1):
        if abs(line[i] - line[i+1]) > 3 or abs(line[i] - line[i+1]) < 1:
            return False
        if (line[i] < line[i + 1] and not asc) or (line[i] > line[i + 1] and asc):
            return False
    return True

safes = 0
for line in lines:
    if isSafeDamp(line):
        safes += 1
print(safes)