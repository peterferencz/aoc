lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()
lines[0] = lines[0].strip()

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "%s --> (%s,%s)" % (self.name, self.left, self.right)

    def __str__(self):
        return "%s --> (%s,%s)" % (self.name, self.left, self.right)

dict = {}
for line in lines[2:]:
    a = line.strip().split(' = ')
    b = a[1][1:-1].split(', ')
    node = Node(a[0], b[0], b[1])
    dict[node.name] = node

onNode = "AAA"
steps = 0
while onNode != "ZZZ":
    t = lines[0][steps % len(lines[0])]
    onNode = dict[onNode].left if t == "L" else dict[onNode].right
    steps += 1
print(steps)