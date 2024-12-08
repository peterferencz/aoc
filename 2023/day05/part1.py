lines = []

with open("input.txt", 'r') as f:
    lines = f.readlines()
lines.append("")

seedsToPlant = list(map(int, lines[0].strip()[7:].split(' ')))

dictionary = {}
path = ['seed-soil', 'soil-fertilizer', 'fertilizer-water', 'water-light', 'light-temperature', 'temperature-humidity', 'humidity-location']

i = 2
while i < len(lines):
    m = lines[i].strip().split('-to-')
    m[1] = m[1][:-5]
    i += 1

    arr = []
    while (line := lines[i].strip()) != "":
        arr.append(list(map(int, line.split(' '))))
        i += 1
    i += 1
    dictionary["%s-%s"% tuple(m)] = arr

def convert(seed, algorithm):
    for r in dictionary[algorithm]:
        if seed in range(r[1], r[1]+r[2]):
            return r[0]+(seed - r[1])
    return seed

# print(list(map(lambda x: len(dictionary[x]), dictionary.keys())))
# exit(0)
# print(convert(14, 'soil-fertilizer'))

low = -1
for seed in seedsToPlant:
    print('seed ' + str(seed))
    for algorithm in path:
        seed = convert(seed, algorithm)
        print(seed)
    if low == -1:
        low = seed
    elif seed < low:
        low = seed
print(low)