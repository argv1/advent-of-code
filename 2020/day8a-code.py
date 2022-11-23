#!/usr/bin/env python3
'''
    advent of code 2020 Day 8 Challenge 1
'''

path, input, res, tmp, n = 'D:/AoC/2020/day8-input.txt', [], None, 0, 0

with open(path, 'r') as f:  
    lines = f.readlines()
    for line in lines:
        input.append([line[:3], int(line[3:].strip()), []])

while(res == None):
    if input[n][2] != []:
        res = tmp
    elif input[n][0] == 'acc':
        input[n][2] = 'x'
        tmp+= input[n][1]
        n+=1
    elif input[n][0] == 'nop':
        input[n][2] = 'x'
        n+=1
    elif input[n][0] == 'jmp':
        input[n][2] = 'x'
        n+= input[n][1]

print(res)