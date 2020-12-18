#!/usr/bin/env python3
'''
    advent of code 2020 Day 3 Challenge 1
'''

res, position = 0, 0
with open('H:/OneDrive/Programme/_current/adventofcode/2020/day3-input.txt', 'r') as f:  
    for line in f:
        line = line.rstrip("\n")
        if(line[position] == '#'): res+=1
        if(position <= (len(line) -4)):
            position+= 3        
        else: 
            position+= 3-len(line)
print(res)