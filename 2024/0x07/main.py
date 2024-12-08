#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 7
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 7)

eq = list(map(lambda l: l.split(' '), aoc.read_lines()))
for l in eq:
    l[0] = l[0][:-1]
eq = [list(map(int, e)) for e in eq]
eq = [[e[0], e[1:]] for e in eq]

# =============================== Part 1 =======================================


def testEq(ans, vals):
    if len(vals) == 1:
        return vals[0] == ans

    v1, v2 = vals[0], vals[1]
    vals = vals[2:]
    if testEq(ans, [v1 + v2, *vals]): return True
    if testEq(ans, [v1 * v2, *vals]): return True
    vals = [v1, v2, *vals]
    return False

s = 0
for e in eq:
    if testEq(e[0], e[1]):
        s += e[0]

aoc.print_part1(s)

# =============================== Part 2 =======================================

def testEq(ans, vals):
    if len(vals) == 1:
        return vals[0] == ans

    v1, v2 = vals[0], vals[1]
    vals = vals[2:]
    if testEq(ans, [v1 + v2, *vals]): return True
    if testEq(ans, [v1 * v2, *vals]): return True
    if testEq(ans, [int(''.join([str(v1), str(v2)])), *vals]): return True
    vals = [v1, v2, *vals]
    return False

s = 0
for e in eq:
    if testEq(e[0], e[1]):
        s += e[0]

aoc.print_part2(s)