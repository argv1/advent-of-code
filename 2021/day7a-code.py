#!/usr/bin/env python3
'''
    advent of code 2021 Day 7 Challenge 1
'''

import statistics

with open('D:/AoC/day7-input.txt', 'r') as f:
    input_data = [line.split(',') for line in f][0]
input_data = [int(entry) for entry in input_data]
median_data = statistics.median(input_data)
res = 0
for entry in input_data:
    res += abs(entry - median_data) 
print(int(res))