#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 1
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 1)

col1, col2 = aoc.read_matrix_int(True)
col1.sort()
col2.sort()

# =============================== Part 1 =======================================

s = 0
for i in range(len(col1)):
    s += abs(col1[i] - col2[i])

aoc.print_part1(s)

# =============================== Part 2 =======================================

appear = {}
for i in range(len(col2)):
    if col2[i] not in appear:
        appear[col2[i]] = 0
    appear[col2[i]] += 1

similarity = 0
for i in range(len(col1)):
    if col1[i] not in appear: continue
    similarity += col1[i] * appear[col1[i]]

aoc.print_part2(similarity)