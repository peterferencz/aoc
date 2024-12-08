lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

obj = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
nums = list(map(lambda n: str(n), range(1, 10)))

def getNum(line):
    # Funny story, I spent 2hrs on figuring out the indexing, but with thextra character, 
    # I don't have to bother with that. Yes, I know I'm a genius
    line = line.strip() + '*'
    n = [0,0]

    print(line)
    for i in range(len(line)):
        if line[i] in nums:
            n[1] = int(line[i])
            if n[0] == 0: n[0] = int(line[i])
        elif i != len(line)-1:
            j = 0
            buff = list(obj.keys())
            while (i+j) <= len(line) and buff != []:
                for number in buff.copy():
                    if len(number) == j:
                        n[1] = obj[line[i:i+j]]
                        if n[0] == 0: n[0] = obj[line[i:i+j]]
                        buff = []
                        break
                    if number[j] != line[i+j]:
                        buff.remove(number)
                j += 1
    return n[0]*10 + n[1]

lines = list(map(getNum, lines))
print(lines)
print(sum(lines))