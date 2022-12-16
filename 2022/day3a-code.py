#!/usr/bin/env python3
'''
    advent of code 2022 Day 3 Challenge 1
'''

with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day3-input.txt", "r") as f:
    lines = [entry.strip('\n') for entry in f.readlines()]
    
score = 0

for line in lines:
    half = int(len(line)/2)
    for n in range(0,half):
        if line[n] in line[half:] and line[n].islower():
            score += ord(line[n]) - 96
            break
        elif line[n] in line[half:] and line[n].isupper():
            score += ord(line[n]) - 38
            break

print(score)