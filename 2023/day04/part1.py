import math


lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = list(map(lambda x: list(map(int, filter(lambda y: y != "", x.split(' ')))), lines[i].strip().split(': ')[1].split(' | ')))

print(sum(math.floor(pow(2, len(list(filter(lambda x: x in lines[i][0] , lines[i][1]))) -1)) for i in range(len(lines))))