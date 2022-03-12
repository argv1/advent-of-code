#!/usr/bin/env python3
'''
    advent of code 2021 Day 9 Challenge 2
'''

import numpy as np

def basin(row, column, counter): 
    if basins[row][column] != 0:
        pass
    else:
        for direction in ("up", "down", "left", "right"):
            basins[row][column] = counter
            if direction == "up" and row > 0 and input_data[row-1][column] != 9:
                basin(row-1, column, counter)
            elif direction == "down" and row < len(input_data)-1 and input_data[row+1][column] != 9:
                basin(row+1, column, counter)            
            elif direction == "left" and column > 0 and input_data[row][column-1] != 9:
                basin(row, column-1, counter)  
            elif direction == "right" and column < len(input_data[row])-1 and input_data[row][column+1] != 9:
                basin(row, column+1, counter)
with open(r'd:\aoc\day9-input.txt', 'r') as f:
    input_data = [list(map(int,line.strip())) for line in f]

global basins 
basins = np.zeros([len(input_data), len(input_data[row])], dtype=int)
counter = 0

for row, line in enumerate(input_data):
    for column, value in enumerate(line):
        if basins[row][column] == 0:
            counter += 1
        if input_data[row][column] == 9:
            basins[row][column] = -1
            counter -= 1
        else:
            basin(row, column, counter) 

unique, counts = np.unique(basins, return_counts=True)
bas = dict(zip(unique, counts))
bas.pop(-1)
top = list(dict(sorted(bas.items(), key=lambda item: item[1],reverse=True)).keys())
bas[top[0]] * bas[top[1]] * bas[top[2]]