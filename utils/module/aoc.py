#!/usr/bin/env python3

import sys
import time

# t : test / p : prod
MODE_TEST = 't'
MODE_PROD = 'p'
MODE = MODE_TEST

FILE = ""

def init(year, day):
    global CEND
    global CYELLOW
    global CGREEN
    global CBLUE
    global AOC_PREFIX
    
    CEND        = '\33[0m'
    CYELLOW     = '\33[33m'
    CGREEN      = '\33[32m'
    CBLUE       = '\33[34m'
    AOC_PREFIX  = f"{CYELLOW}[{CGREEN}AOC{CYELLOW}]{CEND}" 
    print(f"{CYELLOW}========{CGREEN} Advent Of Code{CBLUE} {year} {CYELLOW}| {CGREEN}Day {CBLUE}{day:02} {CYELLOW}========{CEND}")

    tmode = ["d", "dev", "develop", "t",  "test"]
    pmode = ["p", "prod", "production"]

    global startTime
    global part1Time

    startTime = time.time()
    part1Time = time.time()

    if len(sys.argv) < 2:
        MODE = MODE_TEST
    elif sys.argv[1] in tmode:
        MODE = MODE_TEST
    elif sys.argv[1] in pmode:
        MODE = MODE_PROD
    else:
        MODE = MODE_TEST
    
    global FILE
    FILE = "example.txt" if MODE is MODE_TEST else "input.txt"
    
    print(AOC_PREFIX, "Mode:", "test" if MODE is MODE_TEST else "prod")

def read_matrix_char(transposed = False):
    ret = []
    with open(FILE, "r") as f:
        ret = list(map(lambda l: list(l.strip()), f.readlines()))
    if transposed: return [[ret[j][i] for j in range(len(ret))] for i in range(len(ret[0]))]
    else: return ret

def read_matrix_int(transposed = False):
    ret = []
    with open(FILE, "r") as f:
        ret = list(map(lambda l: list(map(int, list( l.strip().split(' ') if ' ' in l else l.strip() ))), f.readlines()))
    if transposed: return [[ret[j][i] for j in range(len(ret))] for i in range(len(ret[0]))]
    else: return ret

def read_line_int():
    with open(FILE, "r") as f:
        return list(map(int, list(f.readline().strip())))

def read_lines():
    with open(FILE, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))

def create_empty_matrix(w, h):
    return [ [0] * w ] * h

def print_matrix(matrix):
    for l in matrix:
        print(" ".join(l))

def print_part1(answer):
    print(AOC_PREFIX, "Solution of part 1: ", answer)
    global part1Time
    part1Time = time.time()

def print_part2(answer):
    print(AOC_PREFIX, "Solution of part 2: ", answer)

    if MODE is MODE_PROD:
        endTime = time.time()
        print(AOC_PREFIX, "Part 1 ran for %.3f" % (part1Time - startTime))
        print(AOC_PREFIX, "Part 2 ran for %.3f" % (endTime - part1Time))
    print(f"{CYELLOW}==============================================")