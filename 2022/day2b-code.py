#!/usr/bin/env python3
'''
    advent of code 2022 Day 2 Challenge 2
'''

with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day2-input.txt", "r") as f:
    lines = [entry.strip('\n').split(' ') for entry in f.readlines()]

repl = {"A": "1",
         "B": "2",
         "C": "3"}

score = 0

for line in lines:
    for key in repl: 
        line[0] = line[0].replace(key, repl[key])

for line in lines:
    if line[1] == "X" and line[0] != "1":
        score += int(line[0]) - 1
    elif line[1] == "X" and line[0] == "1":
        score += 3
    elif line[1] == "Y":
        score += 3 + int(line[0])
    elif line[1] == "Z" and line[0] == "3":
        score += 6 + 1
    elif line[1] == "Z" and line[0] != "3":
        score += 6 + int(line[0]) + 1

print(score)