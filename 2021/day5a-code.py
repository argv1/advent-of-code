#!/usr/bin/env python3
'''
    advent of code 2020 Day 5 Challenge 1
'''

import numpy as np

with open('D:/AoC/day5-input.txt', 'r') as f:
    input_data = [line.rstrip('\n').split(' -> ') for line in f]

board, res = np.zeros((991, 991)), 0

for entry in input_data:    
    y1,x1 = map(int, entry[0].split(","))
    y2,x2 = map(int, entry[1].split(","))   
    if(x1 != x2) and (y1 == y2):
        for x in range(min(x1,x2),max(x1,x2)+1):
            board[x,y1] += 1    
    elif(x1 == x2) and (y1 != y2):
        for y in range(min(y1,y2),max(y1,y2)+1):
            board[x1,y] += 1 
                        
unique, counts = np.unique(board, return_counts=True)
dict(zip(unique, counts))

for entry in counts[2:]:
    res +=entry
    
print(res)