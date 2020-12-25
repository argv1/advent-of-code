#!/usr/bin/env python3
'''
    advent of code 2020 Day 6 Challenge 2
'''

res, n, check, path = 0, -1, '', 'H:/OneDrive/Programme/_current/adventofcode/2020/day6-input.txt'
with open(path, 'r') as f:  
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        n+=1
        if(line != '\n'):
            check += line.lower().rstrip('\n')
        if(line == last or line == '\n'):
            if(line == last): n+=1            
            if(n == 1):
                res+=len(set(check))
            else:
                for entry in set(check):
                    if(check.count(entry) == n):
                        res+=1
            check, n = '', -1
print(res)