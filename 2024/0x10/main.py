#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 10
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 10)

data = aoc.read_matrix_int()
LY = len(data)
LX = len(data[0])

# =============================== Part 1 =======================================

starts = []
for y in range(LY):
    for x in range(LX):
        if data[y][x] == 0:
            starts.append((x, y))

def trailScore(pos, tops):
    x, y = pos
    v = data[y][x]
    if v == 9:
        tops.add(pos)
        return
    if x > 0 and data[y][x-1] == v + 1: trailScore((x-1, y), tops)
    if y > 0 and data[y-1][x] == v + 1: trailScore((x, y-1), tops)
    if x < LX -1 and data[y][x+1] == v + 1: trailScore((x+1, y), tops)
    if y < LY -1 and data[y+1][x] == v + 1: trailScore((x, y+1), tops)
    return

s = 0
for start in starts:
    tops = set()
    trailScore(start, tops)
    s += len(tops)

aoc.print_part1(s)

# =============================== Part 2 =======================================

totalRating = 0
def trailRating(pos):
    x, y = pos
    v = data[y][x]
    s = 0
    if v == 9:
        return 1
    if x > 0 and data[y][x-1] == v + 1: s += trailRating((x-1, y))
    if y > 0 and data[y-1][x] == v + 1: s += trailRating((x, y-1))
    if x < LX -1 and data[y][x+1] == v + 1: s += trailRating((x+1, y))
    if y < LY -1 and data[y+1][x] == v + 1: s += trailRating((x, y+1))
    return s

s = 0
for start in starts:
    s += trailRating(start)

aoc.print_part2(s)