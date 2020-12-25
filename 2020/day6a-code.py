#!/usr/bin/env python3
'''
    advent of code 2020 Day 6 Challenge 1
'''

res, check, path = 0, '', 'D:/Programme/_current/advent-of-code/2020/day6-input.txt'
with open(path, 'r') as f:  
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        if(line != '\n'):
            check += line.lower().rstrip('\n')
        if(line == last or line == '\n'):
            res+=len(set(check))
            check = ''
print(res)