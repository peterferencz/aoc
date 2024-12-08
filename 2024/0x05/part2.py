from functools import cmp_to_key

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

def order(a, b):
    if [a, b] in orders: return -1
    if [b, a] in orders: return 1
    return 0

n = 0
for p in pages:
    if not isInOrder(p):
        p = sorted(p, key=cmp_to_key(order))
        n += p[int(len(p) / 2)]

print(n)

