#!/usr/bin/env python3
'''
    advent of code 2021 Day 9 Challenge 1
'''

with open(r'K:\OneDrive\Programme\_current\advent-of-code\2021\day9-input.txt', 'r') as f:
    input_data = [list(map(int,line.strip())) for line in f]

res = 0
for row, line in enumerate(input_data):
    for count, value in enumerate(line):
        up = input_data[row-1][count] if row != 0 else 9                       
        down = input_data[row+1][count] if row < len(input_data)-1 else 9
        left = input_data[row][count-1] if count != 0 else 9
        right = input_data[row][count+1] if count < len(input_data[row])-1 else 9       
        if(value < up and value < down and value < left and value < right): res += value+1
print(res)