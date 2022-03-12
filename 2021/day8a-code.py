#!/usr/bin/env python3
'''
    advent of code 2021 Day 8 Challenge 1
'''

with open(r'd:\aoc\day8-input.txt', 'r') as f:
    values = [line.strip("\n").split("|")[1].strip(" ").split(" ") for line in f]

res = 0

for entry in [item for sublist in values for item in sublist]:
    if len(entry) == 2 or len(entry) == 3 or len(entry) == 4 or len(entry) == 7:
        res += 1

res