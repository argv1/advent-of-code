#!/usr/bin/env python3
'''
    advent of code 2020 Day 4 Challenge 1
'''

res, check, path = 0, "", 'H:/OneDrive/Programme/_current/adventofcode/2020/day4-input.txt'
with open(path, 'r') as f:  
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        if(line != '\n'):
            check += line.lower().rstrip("\n")
        if(line == last or line == '\n'):
            if("byr:" in check and "iyr:" in check and "eyr:" in check and "hgt:" in check and "hcl:" in check and "ecl:" in check and "pid:" in check):
                res+=1
            check = ""
print(res)