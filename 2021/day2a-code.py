#!/usr/bin/env python3
'''
    advent of code 2021 Day 2 Challenge 1
'''

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day2-input.txt', 'r') as f:
    content = [line.rstrip('\n').rsplit(' ') for line in f]

flat_list = [0,0]
for sublist in content:
    if(sublist[0] == "forward"): flat_list[0] += int(sublist[1])
    elif(sublist[0] == "down"): flat_list[1] += int(sublist[1])       
    else: flat_list[1] -= int(sublist[1])

print(flat_list[0]*flat_list[1])