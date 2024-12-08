lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

games = {}

indicies = {
    "red": 0,
    "green": 1,
    "blue": 2
}

def parse(line):
    line = line.strip().split(':')
    game = int(line[0][5:])
    
    def parseGame(draw):
        toRet = [0,0,0]
        for d in draw.split(','):
            a = d[1:].split(' ')
            toRet[indicies[a[1]]] = int(a[0])
        return toRet
    
    draws = list(map(parseGame, line[1].split(';')))
    
    games[game] = draws

for line in lines:
    parse(line)


p = 0
for id in games.keys():
    m = [0,0,0]
    for game in games[id]:
        m[0] = max(m[0], game[0])
        m[1] = max(m[1], game[1])
        m[2] = max(m[2], game[2])
    p += m[0] * m[1] * m[2]
print(p)
