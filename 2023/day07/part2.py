lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

hands = []
strengths = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
#                                             8   9   10

for line in lines:
    arr = line.strip().split(' ')
    hands.append([arr[0], int(arr[1])])

#  0  Five of a kind, where all five cards have the same label: AAAAA
#  1  Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#  2  Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#  3  Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#  4  Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#  5  One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#  6  High card, where all cards' labels are distinct: 23456
def getType(hand):
    dict = {}
    indexOfJ = strengths.index('J')
    for i in range(len(hand)):
        dict[strengths.index(hand[i])] = dict.get(strengths.index(hand[i]), 0) + 1
        
    if (indexOfJ in dict.keys()) and len(dict.keys()) != 1:
        mostValuable = list(dict.keys())[0]
        for key in filter(lambda y: y != indexOfJ, dict.keys()):
            if dict[key] > dict[mostValuable]:
                mostValuable = key
        dict[mostValuable] += dict[indexOfJ]
        del dict[indexOfJ]

    l = len(dict.keys())
    if l == 1: return 0
    elif l == 2: # 1/2
        if any([(dict[list(dict.keys())[i]] == 4) for i in range(2)]): return 1
        else: return 2
    elif l == 3: # 3/4
        if any([(dict[list(dict.keys())[i]] == 3) for i in range(3)]): return 3
        else: return 4
    elif l == 4: return 5
    elif l == 5: return 6
    else:
        print("err") 
        exit(1)

for i in range(len(hands)):
    hand = hands[i]
    type = getType(hand[0])
    
    # if "J" in hand[0]:
    #     print(hand[0], type)

    #val = type|first card|second card|...
    val = (6 - type) * pow(10, 10) + sum(strengths.index(hand[0][j]) * pow(10, (len(hand[0])-1 - j)*2) for j in range(len(hand[0])))
    hands[i] = [*hand, val]

hands = sorted(hands, key=lambda x: x[2])

s = 0
for i in range(len(hands)):
    s += hands[i][1] * (i+1)
print(s)