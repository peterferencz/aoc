import re

lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

product = 0
en = True
for line in lines:
    for match in re.findall("(mul\((\d*)\,(\d*)\))|(do\(\))|(don\'t\(\))", line):
        print(match)
        if match[0] != "":
            if en:
                product += int(match[1]) * int(match[2])
        elif match[3] != "":
            en = True
        elif match[4] != "":
            en = False

print("Product: ", product)