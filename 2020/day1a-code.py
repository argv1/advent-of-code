#!/usr/bin/env python3
'''
    advent of code 2020 Day 1 Challenge 1
'''

with open('H:/OneDrive/Programme/_current/adventofcode/day1-input.txt', 'r') as f:
    content = [int(line.rstrip('\n')) for line in f]

for idx, entry in enumerate(content):
    for n in range(idx,len(content)):
        if(entry + content[n] == 2020):
            print(f"{entry}, {content[n]}")               
            print(entry*content[n])
            break