#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 6
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 6)

lab = aoc.read_matrix_char()

start_x, start_y, start_dx, start_dy = 0, 0, 0, -1
for y in range(len(lab)):
    for x in range(len(lab[y])):
        if lab[y][x] == '^':
            start_x = x
            start_y = y

# =============================== Part 1 =======================================

def positions():
    visited = set()
    x, y, dx, dy = start_x, start_y, start_dx, start_dy
    while( 0 <= x+dx < len(lab[0]) and 0 <= y+dy < len(lab)):
        if (x, y) not in visited:
            visited.add((x, y))
        
        if lab[y + dy][x+dx] == '#':
            dx, dy = -dy, dx # rot cw 90deg
        x += dx
        y += dy
    visited.add((x, y))
    return visited

aoc.print_part1(len(positions()))

# =============================== Part 2 =======================================

def terminates():
    visited = set()
    x, y, dx, dy = start_x, start_y, start_dx, start_dy
    while(0 <= x+dx < len(lab[0]) and 0 <= y+dy < len(lab)):
        
        if (x, y, dx, dy) in visited: return False
        visited.add((x, y, dx, dy))
        
        if lab[y + dy][x+dx] == '#':
            dx, dy = -dy, dx # rot cw 90deg

        visited.add((x, y, dx, dy))
        
        
        x += dx
        y += dy
    return True

s = 0
for pos in positions():
    if lab[pos[1]][pos[0]] != '.': continue
    lab[pos[1]][pos[0]] = '#'
    if not terminates():
        s += 1
    lab[pos[1]][pos[0]] = '.'

aoc.print_part2(s)