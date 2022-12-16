#!/usr/bin/env python3
'''
    advent of code 2022 Day 3 Challenge 2
'''

with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day3-input.txt", "r") as f:
    lines = [entry.strip('\n') for entry in f.readlines()]
    
score = 0


for n in range(0,len(lines)):
    if n+2 < len(lines) and (n+3)%3 == 0:
        for item in lines[n]:
            if item in lines[n+1] and item in lines[n+2]:
                if item.islower():
                    score += ord(item) - 96
                    break
                elif item.isupper():
                    score += ord(item) - 38
                    break

print(score)