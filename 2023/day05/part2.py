lines = []

with open("input.txt", 'r') as f:
    lines = f.readlines()
lines.append("")


seedsToPlant = list(map(int, lines[0].strip()[7:].split(' ')))
seedsToPlant = list(zip(seedsToPlant, seedsToPlant[1:]))[::2]
seedsToPlant = list(map(lambda x: [x[0], x[0]+x[1]-1], seedsToPlant))

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

    arr = list(map(lambda x: [[x[1], x[1]+x[2]], x[0]-x[1]], arr))
    dictionary["%s-%s"% tuple(m)] = arr


def offset(rang, amount):
    return [rang[0] + amount, rang[1] + amount]

def offsetOverlap(range1, range2, amount):
    # print(range1, range2, amount)
    ret = offset([max(range1[0], range2[0]), min(range1[1], range2[1])], amount)
    return [] if (ret[0] > ret[1] or ret[1] < ret[0]) else ret

# range - range --> [range, range]
def subtractRange(fromThis, subtractThis):
    r1,r2 = [],[]
    if fromThis[0] < subtractThis[0]:
        r1 = [fromThis[0], min(subtractThis[0] -1, fromThis[1])]
    if fromThis[1] > subtractThis[1]:
        r2 = [max(subtractThis[1]+1, fromThis[0]), fromThis[1]]
    if r1 == []: return r2
    if r2 == []: return r1
    else: return [r1, r2]

# [range] - range --> [[range]]
def subtractOneRange(fromThese, this):
    ret = []
    for f in fromThese:
        val = subtractRange(f, this)
        if val == []: continue
        if type(val[0]) == list:
            ret.extend(val)
        else:
            ret.append(val)
    return ret

# range[] - range[] --> 
def subtractRanges(fromThese, subtractThese):
    for that in subtractThese:
        fromThese = subtractOneRange(fromThese, that)
    return list(filter(lambda x: x != [] , fromThese))

def getRangesForRule(ranges, r):
    newRange = []
    for rang in ranges:
        rules = dictionary[r]
        for rule in rules:
            newRange.append(offsetOverlap(rang, rule[0], rule[1]))
        newRange.extend(subtractRanges([rang], list(map(lambda x: x[0], rules))))
    return list(filter(lambda x: x != [], newRange))

for p in path:
    seedsToPlant = getRangesForRule(seedsToPlant, p)

m = -1
for location in seedsToPlant:
    if m == -1:
        m = location[0]
    elif location[0] < m:
        m = location[0]
print(m)