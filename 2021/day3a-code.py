#!/usr/bin/env python3
'''
    advent of code 2021 Day 3 Challenge 1
'''

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day3-input.txt', 'r') as f:
    content = f.read()

# transpose to reduce iterations
trans_con = [''.join(chars) for chars in zip(*content.splitlines())]

gamma, epsilon, size = '', '', len(content.splitlines())

''' 
    The assignment operator (and all variations on it) forms a statement in Python, not an expression. 
    Unfortunately, list comprehensions (and other comprehensions, like set, dictionary and generators) only support expressions.
'''
    
for n in range(0,len(trans_con)): 
    if trans_con[n].count('0') > size/2:
        gamma += str(0)
        epsilon += str(1)
    else:
        gamma += str(1)
        epsilon += str(0)
        
print(int(gamma, 2) * int(epsilon, 2))