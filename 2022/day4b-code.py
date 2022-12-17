#!/usr/bin/env python3
'''
    Advent of Code 2022 Day 4 Challenge 2
'''

with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day4-input.txt", "r") as f: #day4-input
    lines = [entry.strip('\n') for entry in f.readlines()]

score = 0    
    
for line in lines:
    a, b = line.split(",")
    a_min, a_max = a.split("-")
    b_min, b_max = b.split("-")
    if (int(a_min) <= int(b_min) and int(a_max) >= int(b_min)) or (int(b_min) <= int(a_min) and int(b_max) >= int(a_min)):
        score += 1

print(score)