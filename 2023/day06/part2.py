lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

time = int("".join(list(filter(lambda x: x!= " ", lines[0].strip()[11:]))))
distance = int("".join(list(filter(lambda x: x!= " ", lines[1].strip()[11:]))))

val = 0
for t in range(1, time):
    if (time - t) * t > distance:
        val += 1
print(val)
