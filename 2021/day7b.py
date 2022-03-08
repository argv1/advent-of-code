#!/usr/bin/env python3
'''
    advent of code 2021 Day 7 Challenge 2
'''

with open(r'K:\OneDrive\Programme\_current\advent-of-code\2021\day7-input.txt', 'r') as f:
    input_data = [line.split(',') for line in f][0]
input_data = [int(entry) for entry in input_data]
maximum = max(input_data)
res = 1000000000000
for n in range(1,maximum):
    tmp = 0
    for entry in input_data:
        tmp += sum(range(1,abs(entry - n)+1))
    if tmp < res:
        res = tmp
print(res)