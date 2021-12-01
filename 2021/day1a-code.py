#!/usr/bin/env python3
'''
    advent of code 2021 Day 1 Challenge 1
'''

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day1-input.txt', 'r') as f:
    content = [int(line.rstrip('\n')) for line in f]

print(len([entry for idx, entry in enumerate(content) if(entry > content[idx-1])]))
