orders = []
pages = []
with open("input.txt", "r") as f:
    ord = True
    for l in f.readlines():
        l = l.strip()
        if ord:
            if l == "":
                ord = False
                continue
            orders.append(list(map(int, l.split('|'))))
        else:
            pages.append(list(map(int, l.split(','))))

def isInOrder(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if [list[j], list[i]] in orders: return False
    return True

n = 0
for p in pages:
    if isInOrder(p):
        print(p)
        n += p[int(len(p) / 2)]

print(n)

