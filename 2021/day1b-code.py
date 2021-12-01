#!/usr/bin/env python3
'''
    advent of code 2021 Day 1 Challenge 1 Part two
'''

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day1-input.txt', 'r') as f:
    content = [int(line.rstrip('\n')) for line in f]

con_agg = [sum(content[i:i+3]) for i in range(len(content))]  # <-- thx to github.com/rogall-e/
print(len([entry for idx, entry in enumerate(con_agg) if(entry > con_agg[idx-1])]))