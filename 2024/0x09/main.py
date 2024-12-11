#!/usr/bin/env python3
# ==============================================================================
# Made for Advent of Code 2024, day 9
# ==============================================================================
import utils.aoc as aoc

aoc.init(2024, 9)

data = aoc.read_line_int()
parity = len(data) % 2 == 0

expanded = []
fileId = 0
for i in range(len(data)):
    if i % 2 == 0: # file
        for i in range(data[i]):
            expanded.append(fileId)
        fileId += 1
    else: # empty space
        for _ in range(data[i]):
            expanded.append('.')


# =============================== Part 1 =======================================

def compact():
    L = len(expanded)
    front_free = 0
    back_file = -1
    while True:
        while expanded[front_free] != '.' and front_free < L-1: front_free += 1
        while expanded[back_file] == '.': back_file -= 1
        if front_free >= L + back_file: break

        # compact data
        expanded[front_free] = expanded[back_file]
        expanded[back_file] = '.'

def checksum():
    s = 0
    for i in range(len(expanded)):
        if expanded[i] == '.': continue
        s += i * expanded[i]
    return s

compact()

aoc.print_part1(checksum())

# =============================== Part 2 =======================================

files = {}
expanded = []
fileId = 0
for i in range(len(data)):
    if i % 2 == 0: # file
        for _ in range(data[i]):
            expanded.append(fileId)
        files[fileId] = data[i]
        fileId += 1
    else: # empty space
        for _ in range(data[i]):
            expanded.append('.')


def compact():
    L = len(expanded)

    for id in sorted(files.keys(), reverse=True):
        size = files[id]

        front_free = 0
        while True:
            # find next free space
            while front_free < L-1 and expanded[front_free] != '.': front_free += 1
            if front_free >= L: break

            # find size of free space
            i = front_free
            s = 0
            while i < L and expanded[i] == '.':
                s += 1
                i += 1
            if s >= size: break
            if i >= L:
                front_free = L
                break
            front_free += 1
            

        if front_free >= L: continue

        back_file = -1
        while expanded[back_file] != id: back_file -= 1
        if front_free >= L +back_file: continue
        for j in range(size):
            expanded[front_free+j] = id
            expanded[back_file-j] = '.'

compact()
aoc.print_part2(checksum())