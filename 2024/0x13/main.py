#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 13
# ==============================================================================
import utils.aoc as aoc
import re

aoc.init(2024, 13)

claws = []
machine = []
ind = 0
with open(aoc.FILE, 'r') as f:
    for line in f.readlines():
        if line == "\n": continue

        if ind == 0 or ind == 1:
            machine.append(list(map(int, re.findall("Button [A|B]: X\+(\d+), Y\+(\d+)", line)[0])))
            ind += 1
        else:
            machine.append(list(map(int, re.findall("Prize: X=(\d+), Y=(\d+)", line)[0])))
            claws.append(machine)
            machine = []
            ind = 0

# =============================== Part 1 =======================================

def price(claw):
    # solve claw[0][0] * A + claw[1][0] * B = claw[2][0]
    #       claw[0][1] * A + claw[1][1] * B = claw[2][1]
    Ax, Ay = claw[0][0], claw[0][1]
    Bx, By = claw[1][0], claw[1][1]
    Sx, Sy = claw[2][0], claw[2][1]

    B = [Sy*Ax - Sx*Ay, Ax*By - Bx*Ay]

    if not (B[0]/B[1]).is_integer():
        return 0
    B = B[0]/B[1]
    
    A = (Sx - Bx*B) / Ax
    if not A.is_integer():
        return 0
    
    return 3 * int(A) + int(B)

aoc.print_part1(sum(price(claw) for claw in claws))

# =============================== Part 2 =======================================

for claw in claws:
    claw[2][0] += 10000000000000
    claw[2][1] += 10000000000000

aoc.print_part2(sum(price(claw) for claw in claws))