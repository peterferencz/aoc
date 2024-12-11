#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 11
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 11)

stones = aoc.read_matrix_int()[0]

# =============================== Part 1 =======================================

def blink(stones):
    new = []
    for stone in stones:
        if stone == 0:
            new.append(1)
        elif (l := len(str(stone))) % 2 == 0:
            new.append(int(str(stone)[:int(l/2)]))
            new.append(int(str(stone)[int(l/2):]))
        else:
            new.append(stone * 2024)
    return new


for _ in range(25):
    stones = blink(stones)

aoc.print_part1(len(stones))

# =============================== Part 2 =======================================

from functools import cache

stones = aoc.read_matrix_int()[0]
stones = [x for x in stones if x != ' ']

def blink(stone):
    if stone == 0:
        return [1]
    s = str(stone)
    l = len(s)
    if l % 2 == 0:
        return [ int(s[:l//2]), int(s[l//2:])]
    else:
        return [stone * 2024]

@cache
def numOfSplits(n, remaining):
    if remaining == 0: return 1
    return sum( numOfSplits(s, remaining-1) for s in blink(n))

aoc.print_part2(sum(numOfSplits(stone, 75) for stone in stones))