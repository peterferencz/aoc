import re

lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

product = 0
for line in lines:
    for match in re.findall("mul\((\d*)\,(\d*)\)", line):
        product += int(match[0]) * int(match[1])

print("Product: ", product)