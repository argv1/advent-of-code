#!/usr/bin/env python3
'''
    advent of code 2020 Day 3 Challenge 2
'''

res, position, right, down = [0,0,0,0,0], [1,1,1,1,1], [1,3,5,7,1], 0
with open('H:/OneDrive/Programme/_current/adventofcode/2020/day3-input.txt', 'r') as f:  
    for line in f:
        line = line.rstrip("\n")
        for entry in range(0,5):
            if(entry == 4 and down%2 != 0):
                continue         
            if(line[position[entry]-1] == '#'): 
                res[entry]+=1
            if(position[entry] <= (len(line) -right[entry])):
                position[entry]+= right[entry]        
            else: 
                position[entry]+= right[entry]-len(line)
        down+=1
print(res[0]*res[1]*res[2]*res[3]*res[4])