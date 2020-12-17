#!/usr/bin/env python3
'''
    advent of code 2020 Day 2 Challenge 2
'''

import re

res = 0
with open('H:/OneDrive/Programme/_current/adventofcode/day2-input.txt', 'r') as f:
    for line in f:
        result = re.search('^(\d+)-(\d+)\s(\w):\s(\w+)', line)
        if(result.groups()[3][int(result.groups()[0])-1] == result.groups()[2] and result.groups()[3][int(result.groups()[1])-1] != result.groups()[2] or result.groups()[3][int(result.groups()[0])-1] != result.groups()[2] and result.groups()[3][int(result.groups()[1])-1] == result.groups()[2]):
            res+=1
    print(res)