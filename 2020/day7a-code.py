#!/usr/bin/env python3
'''
    advent of code 2020 Day 7 Challenge 1
'''
import re

res, colors, path = 0, [], 'H:/OneDrive/Programme/_current/adventofcode/2020/day7-input.txt'
with open(path, 'r') as f:  
    lines = f.readlines()
    for line in lines:
        tmp = re.search('^(.*) bags contain .* shiny gold', line)
        if(tmp):
            colors.append(tmp.groups()[0])  
    for color in colors:    
        for line in lines:
            tmp = re.search(f'^(.*) bags contain .* {color}', line)
            if(tmp):
                colors.append(tmp.groups()[0])   
    print(len(set(colors)))
#print(res)