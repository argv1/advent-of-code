#!/usr/bin/env python3
'''
    advent of code 2021 Day 1 Challenge 1 Part two
'''

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day1-input.txt', 'r') as f:
    content = [int(line.rstrip('\n')) for line in f]

res = 0

res = [1 for idx, entry in enumerate(content) if(content[idx] + content[idx-1] + content[idx-2] > content[idx-1] + content[idx-2] + content[idx-3])]
print(len(res))