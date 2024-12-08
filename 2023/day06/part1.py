lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

times = list(map(int, filter(lambda x: x != '', lines[0].strip()[11:].split(' '))))
distances = list(map(int, filter(lambda x: x != '', lines[1].strip()[11:].split(' '))))
races = [[times[i], distances[i]] for i in range(len(times))]

val = 1
for race in races:
    r = 0
    for time in range(1, race[0]):
        if (race[0] - time) * time > race[1]:
            r += 1
    val *= r
    print(r)
print(val)
