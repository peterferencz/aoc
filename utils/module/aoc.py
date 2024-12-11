#!/usr/bin/env python3

import sys
import time

# t : test / p : prod
MODE_TEST = 't'
MODE_PROD = 'p'

CEND        = '\33[0m'
CYELLOW     = '\33[33m'
CGREEN      = '\33[32m'
CBLUE       = '\33[34m'
AOC_PREFIX  = f"{CYELLOW}[{CGREEN}AOC{CYELLOW}]{CEND}" 

def init(year, day):
    print(f"{CYELLOW}========{CGREEN} Advent Of Code{CBLUE} {year} {CYELLOW}| {CGREEN}Day {CBLUE}{day:02} {CYELLOW}========{CEND}")

    tmode = ["d", "dev", "develop", "t",  "test"]
    pmode = ["p", "prod", "production"]

    global mode
    global startTime
    global part1Time

    startTime = time.time()
    part1Time = time.time()

    if len(sys.argv) < 2:
        mode = MODE_TEST
    elif sys.argv[1] in tmode:
        mode = MODE_TEST
    elif sys.argv[1] in pmode:
        mode = MODE_PROD
    else:
        mode = MODE_TEST
    
    print(AOC_PREFIX, "Mode:", "test" if mode is MODE_TEST else "prod")

def read_matrix_char(transposed = False):
    ret = []
    with open("example.txt" if mode is MODE_TEST else "input.txt", "r") as f:
        ret = list(map(lambda l: list(l.strip()), f.readlines()))
    if transposed: return [[ret[j][i] for j in range(len(ret))] for i in range(len(ret[0]))]
    else: return ret

def read_matrix_int(transposed = False):
    ret = []
    with open("example.txt" if mode == MODE_TEST else "input.txt", "r") as f:
        ret = list(map(lambda l: list(map(int, list( l.strip().split(' ') if ' ' in l else l.strip() ))), f.readlines()))
    if transposed: return [[ret[j][i] for j in range(len(ret))] for i in range(len(ret[0]))]
    else: return ret

def read_line_int():
    with open("example.txt" if mode == MODE_TEST else "input.txt", "r") as f:
        return list(map(int, list(f.readline().strip())))

def read_lines():
    with open("example.txt" if mode == MODE_TEST else "input.txt", "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))

def print_matrix(matrix):
    for l in matrix:
        print(" ".join(l))

def print_part1(answer):
    print(AOC_PREFIX, "Solution of part 1: ", answer)
    global part1Time
    part1Time = time.time()

def print_part2(answer):
    print(AOC_PREFIX, "Solution of part 2: ", answer)

    if mode == MODE_PROD:
        endTime = time.time()
        print(AOC_PREFIX, "Part 1 ran for %.3f" % (part1Time - startTime))
        print(AOC_PREFIX, "Part 2 ran for %.3f" % (endTime - part1Time))
    print(f"{CYELLOW}==============================================")