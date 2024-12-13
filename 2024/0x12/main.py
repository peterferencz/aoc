#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 12
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 12)

garden = aoc.read_matrix_char()
LY, LX = len(garden), len(garden[0])

# =============================== Part 1 =======================================


was = set()

def proc(x, y):
    if (x, y) in was: return (0, 0)
    was.add((x, y))
    p = 0
    a = 0
    type = garden[y][x]

    if y != 0 and garden[y-1][x] == type:
        _p, _a = proc(x, y-1)
        p += _p
        a += _a
    else:
        p += 1

    if y != LY-1 and garden[y+1][x] == type:
        _p, _a = proc(x, y+1)
        p += _p
        a += _a
    else:
        p += 1

    if x != 0 and garden[y][x-1] == type:
        _p, _a = proc(x-1, y)
        p += _p
        a += _a
    else:
        p += 1

    if x != LX-1 and garden[y][x+1] == type:
        _p, _a = proc(x+1, y)
        p += _p
        a += _a
    else:
        p += 1

    return (p, a+1)

s = 0
for y in range(LY):
    for x in range(LX):
        p, a = proc(x, y)
        s += p * a

aoc.print_part1(s)

# =============================== Part 2 =======================================

was = set()

# l, r, t, b
def proc(x, y, d):
    if (x, y, d) in was: return ([0,0,0,0], 0)
    was.add((x, y, d))
    p = [0, 0, 0, 0]
    a = 0
    type = garden[y][x]

    if y != 0 and garden[y-1][x] == type and (d == 0 or d == 1):
        _p, _a = proc(x, y-1, d)
        p = [p[i] + _p[i] for i in range(4)]
        a += _a
    else:
        p[d] += 1

    if y != LY-1 and garden[y+1][x] == type and (d == 0 or d == 1):
        _p, _a = proc(x, y+1, d)
        p = [p[i] + _p[i] for i in range(4)]
        a += _a
    else:
        p[d] += 1

    if x != 0 and garden[y][x-1] == type and (d == 2 or d == 3):
        _p, _a = proc(x-1, y, d)
        p = [p[i] + _p[i] for i in range(4)]
        a += _a
    else:
        p[d] += 1

    if x != LX-1 and garden[y][x+1] == type and (d == 2 or d == 3):
        _p, _a = proc(x+1, y, d)
        p = [p[i] + _p[i] for i in range(4)]
        a += _a
    else:
        p[d] += 1

    return (p, a+1)

s = 0
for y in range(LY):
    for x in range(LX):
        for d in range(4):
            p, a = proc(x, y, d)
            if sum(p) != 0 and a != 0: print(garden[y][x], p, a)
            s += int(sum(p) * a/4)

aoc.print_part2(s)