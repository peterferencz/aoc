#!/usr/bin/env python3

import sys
import time
import datetime
import os
from os.path import join as pjoin
import shutil
from pathlib import Path


today = datetime.date.today()
year = today.year
day = 0


if(len(sys.argv) < 2):
    day = today.day
else:
    try:
        day = int(sys.argv[1])
    except:
        print("Usage: gen.py [day] [year]")
        exit(1)
    if not (0 < day <= 24):
        print("Usage: gen.py [day] [year]")
        exit(1)
if(len(sys.argv) > 2):
    year = int(sys.argv[2])


print(f"Generating files for AOC{year} day {day}...")

yearpath = pjoin(os.path.abspath(os.getcwd()), str(year))

if not os.path.exists(yearpath):
    os.mkdir(yearpath)

daypath = pjoin(yearpath, f"0x{day:02}")
if not os.path.exists(daypath):
    os.mkdir(daypath)

templateFile = pjoin(daypath, "main.py")

utilsFolder = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(templateFile):
    shutil.copyfile(pjoin(utilsFolder, "template.py"), templateFile)

if not os.path.exists(pjoin(daypath, "example.txt")):
    Path(pjoin(daypath, "example.txt")).touch()
if not os.path.exists(pjoin(daypath, "input.txt")):
    Path(pjoin(daypath, "input.txt")).touch()


with open(templateFile, 'r') as f:
  filedata = f.read()

filedata = filedata.replace("__YEAR__", str(year)).replace("__DAY__", str(day))

with open(templateFile, 'w') as f:
  f.write(filedata)

modulefolder = pjoin(utilsFolder, "module")

# link custom module
if not os.path.exists(pjoin(daypath, "utils")):
    os.symlink(modulefolder, pjoin(daypath, "utils"))

print("Created %s" % daypath)