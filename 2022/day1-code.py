#!/usr/bin/env python3
'''
    advent of code 2022 Day 1
'''

res, n = [0], 0

with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day1-input.txt", "r") as f:
    for line in f:
        if line == "\n":
            n+=1
            res.append(0)
        else:
            res[n]+=int(line.rstrip('\n')) 
            
# Challenge 1            
print(max(res))

# Challenge 2
print(sum(sorted(res, reverse=True)[:3]))