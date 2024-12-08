words = []
with open("input.txt", "r") as f:
    words = list(map(lambda x: x.strip(), f.readlines()))

SEARCH = "XMAS"

def checkxmas(x, y):
    if words[y][x] != 'X': return 0
    n = 0


    for dx in range(-1, 2):
        for dy in range(-1, 2):
            l = len(SEARCH)
            if y + dy*(l-1) < 0: continue # circumvent pyhton
            if x + dx*(l-1) < 0: continue # negative indexing
            if y + dy*(l-1) >= len(words): continue # over indexing
            if x + dx*(l-1) >= len(words[y]): continue # over indexing
            
            found = True
            for i in range(len(SEARCH)):
                if words[y + dy*i][x + dx*i] != SEARCH[i]:
                    found = False
                    break
            if(found):
                n += 1

    return n

n = 0
for y in range(len(words)):
    for x in range(len(words[y])):
        n += checkxmas(x,y)

print("XMAS count: ", n)