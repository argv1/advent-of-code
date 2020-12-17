#!/usr/bin/env python3
'''
    advent of code 2020 Day 2 Challenge 1
'''

import re

res = 0
with open('H:/OneDrive/Programme/_current/adventofcode/day2-input.txt', 'r') as f:
    for line in f:
        result = re.search('^(\d+)-(\d+)\s(\w):\s(\w+)', line)
        if (result.groups()[3].count(result.groups()[2]) >= int(result.groups()[0]) and result.groups()[3].count(result.groups()[2]) <= int(result.groups()[1])):
            res+=1
    print(res)