#!/usr/bin/env python3
'''
    advent of code 2020 Day 4 Challenge 1
'''
import re

def check_pass(check):
    pattern = ['byr:(\d{4})','iyr:(\d{4})','eyr:(\d{4})']
    valid_entries = [[1920,2002],[2010,2020],[2020,2030]]
    validation = 0
    if("byr:" in check and "iyr:" in check and "eyr:" in check and "hgt:" in check and "hcl:" in check and "ecl:" in check and "pid:" in check):
        for entry in range(0,3):
            match = int(re.search(pattern[entry], check).groups()[0])
            if(valid_entries[entry][0] <= match <= valid_entries[entry][1]):
                validation +=1

        match = re.search('hgt:(\d{2,3})(\w{2})', check)
        if(match):   
            height, meas = int(match.groups()[0]), match.groups()[1]
            if((meas == "cm" and 150 <= height <= 193) or (meas == "in" and 59 <= height <= 76)):
                validation +=1       

        match = re.search('hcl:#([a-f0-9]{6,7})', check)
        if(match and len(match.groups()[0]) == 6):
            validation +=1                       

        match = re.search('ecl:(\w{3})', check)
        if(match and match.groups()[0] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            validation +=1           

        match = re.search('pid:([0-9]{9,10})', check)
        if(match and len(match.groups()[0]) == 9):
            validation +=1    

        if(validation == 7):
            return True
                
res, check, path = 0, "", 'H:/OneDrive/Programme/_current/adventofcode/2020/day4-input.txt'
with open(path, 'r') as f:  
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        if(line != '\n'):
            check += line.lower().replace("\n", " ")
        if(line == last or line == '\n'):
            if(check_pass(check)):
                res+=1
            check = ""
print(res)