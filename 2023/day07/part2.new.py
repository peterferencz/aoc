lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

def getType(hand):
    if hand == "JJJJJ": return 0
    numberOfJokers = hand.count("J")

    hand = list(filter(lambda x: x != "J", hand))
    val = list(map(lambda x: hand.count(x), hand))
    val[val.index(max(val))] += numberOfJokers

    if 5 in val: return 0 # 5 of a kind
    if 4 in val: return 1 # 4 of a kind
    if 3 in val:
        if 2 in val: return 3 # full house
        return 2 # 3 of a kind
    if 2 in val:
        if len(list(filter(lambda x: x == 2, val))) == 4: return 3 # two pairs
        return 4 # one pair
    return 5 # high card

strengths = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
def getStrength(hand):
    type = getType(hand)
    return (6 - type) * pow(10, 11) + sum(strengths.index(hand[j]) * pow(10, (len(hand)-1 - j)*2) for j in range(len(hand)))

for i in range(len(lines)):
    hand, bid = lines[i].strip().split(' ')
    lines[i] = [hand, int(bid), getStrength(hand)]

lines = sorted(lines, key=lambda x: x[2])
for line in lines:
    print(line)

s = 0
for i in range(len(lines)):
    s += (i+1) * lines[i][1]
print(s)