#!/usr/bin/env python3
'''
    advent of code 2020 Day 1 Challenge 2
'''

with open('H:/OneDrive/Programme/_current/adventofcode/day1-input.txt', 'r') as f:
    content = [int(line.rstrip('\n')) for line in f]

for idx, entry in enumerate(content):
    for m in range(idx,len(content)):
        for n in range(m,len(content)):
            if(entry + content[m] + content[n] == 2020):
                print(f"{entry}, {content[m]}, {content[n]}")               
                print(entry*content[m]*content[n])
                break