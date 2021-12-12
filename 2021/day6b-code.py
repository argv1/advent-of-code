#!/usr/bin/env python3
'''
    advent of code 2021 Day 6 Challenge 2
'''

res = 0
with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day6-input.txt', 'r') as f:
    input_data = [int(entry) for line in f for entry in line[::2]]
    di = {n: input_data.count(n) for n in range(0,9)}

for n in range(0,256):
    tmp = di[0]
    for num in range(1,9):
        di[num-1] = di[num]
    di[8] = tmp
    di[6] += tmp  
for entry in di.values():
    res += entry
   
print(res)