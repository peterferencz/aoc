lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

games = {}

indicies = {
    "blue": 0,
    "red": 1,
    "green": 2
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

print(sum(filter(lambda id: all((game[0] <= 14 and game[1] <= 12 and game[2] <= 13) for game in games[id]),  games.keys())))