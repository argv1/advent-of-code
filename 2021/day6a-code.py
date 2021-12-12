#!/usr/bin/env python3
'''
    advent of code 2021 Day 6 Challenge 1
'''

flat_list = []
with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day6-input.txt', 'r') as f:
    input_data = [int(entry) for line in f for entry in line[::2]]

for n in range(0,80):
    for idx, fish in enumerate(input_data):
        if fish == 0:
            input_data.append(9)
            input_data[idx] = 6
        else:
            input_data[idx] -= 1

print(len(input_data))