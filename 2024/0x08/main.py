#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 8
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 8)

m = aoc.read_matrix_char()
LY = len(m)
LX = len(m[0])

antennas = {}

for y in range(LY):
    for x in range(LX):
        if m[y][x] == '.': continue
        if not m[y][x] in antennas:
            antennas[m[y][x]] = []
        antennas[m[y][x]].append((x, y))

# =============================== Part 1 =======================================

def getAntinotes(a1, a2):
    points = set()
    s = (a1[1] - a2[1]) / (a1[0] - a2[0])
    b = s * a1[0] - a1[1]
    for y in range(LY):
        for x in range(LX):
            if not abs(y - (s*x - b)) < 0.0001: continue    # not in line
            #if m[y][x] != '.': continue
            c1 = pow(a1[0] - x ,2) + pow(a1[1] - y ,2)
            c2 = pow(a2[0] - x ,2) + pow(a2[1] - y ,2)

            if c1 == 4 * c2 or 4 * c1 == c2:
                points.add((x, y))
    return list(points)

anti = set()
for a in antennas:
    for i in range(len(antennas[a])):
        for j in range(i+1, len(antennas[a])):
            pos = getAntinotes(antennas[a][i], antennas[a][j])
            anti = anti.union(pos)

aoc.print_part1(len(anti))

# =============================== Part 2 =======================================

def getAntinotes(a1, a2):
    points = set()
    d = (a1[0] - a2[0], a1[1] - a2[1])
    for y in range(LY):
        for x in range(LX):
            
            # Could be optimized
            for n in range(-LX, LX):
                if (x == a1[0] + d[0] * n) and (y == a1[1] + d[1] * n):
                    points.add((x, y))

    return list(points)

anti = set()
for a in antennas:
    for i in range(len(antennas[a])):
        for j in range(i+1, len(antennas[a])):
            pos = getAntinotes(antennas[a][i], antennas[a][j])
            anti = anti.union(pos)

aoc.print_part2(len(anti))