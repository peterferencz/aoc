words = []
with open("input.txt", "r") as f:
    words = list(map(lambda x: x.strip(), f.readlines()))

def checkxmas(x, y):
    if words[y][x] != 'A': return False
    
    m = 0
    s = 0

    if words[y + 1][x + 1] == 'M': m += 1
    if words[y + 1][x + 1] == 'S': s += 1

    if words[y - 1][x + 1] == 'M': m += 1
    if words[y - 1][x + 1] == 'S': s += 1

    if words[y - 1][x - 1] == 'M': m += 1
    if words[y - 1][x - 1] == 'S': s += 1

    if words[y + 1][x - 1] == 'M': m += 1
    if words[y + 1][x - 1] == 'S': s += 1

    # Filter out  S M
    #              A
    #             M S
    if words[y + 1][x + 1] == words[y - 1][x - 1]: return False

    return m == 2 and s == 2

n = 0
for y in range(1, len(words)-1):
    for x in range(1, len(words[y])-1):
        if checkxmas(x,y):
            n += 1

print("X-MAS count: ", n)