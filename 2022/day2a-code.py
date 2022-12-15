#!/usr/bin/env python3
'''
    advent of code 2022 Day 2 Challenge 1
'''

with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day2-input.txt", "r") as f:
    lines = [entry.strip('\n').split(' ') for entry in f.readlines()]

repl = {"A": "1",
         "B": "2",
         "C": "3",
         "X": "1",
         "Y": "2",
         "Z": "3"}

score = 0

for line in lines:
    for key in repl: 
        line[0] = line[0].replace(key, repl[key])
        line[1] = line[1].replace(key, repl[key])

for line in lines:
    if line[0] == line[1]:  
        score += 3 + int(line[1])
        continue          
    elif (int(line[0]) > int(line[1]) and line[1] != "1") or (line[1] == "1" and line[0] != "3") or (line[0] == "1" and line[1] == "3"):
        score += int(line[1])
        continue
    elif (int(line[0]) < int(line[1]) and line[0] != "1") or (line[0] == "1" and line[1] != "3") or (line[1] == "1" and line[0] == "3"):
        score += 6 + int(line[1])
        continue
    else:
        print(f"{line[0]}: {line[1]}")
        
print(score)