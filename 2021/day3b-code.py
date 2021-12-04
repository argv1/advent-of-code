#!/usr/bin/env python3
'''
    advent of code 2021 Day 3 Challenge 2
'''

def most_com(content, n):
    trans_con = [''.join(chars) for chars in zip(*content)]
    size = len(content)
    if trans_con[n].count('0') > size/2:
        return(0, 1)
    else:
        return(1, 0)

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day3-input.txt', 'r') as f:
    o2_con = f.read().split('\n')
    co2_con = o2_con
o2, co2, n = '', '', 0
  
while(len(o2_con) > 1): 
    o2_tmp = []
    common, lcommon = most_com(o2_con, n)
    for line in o2_con:
        if(line[n] == "0" and common == 0) or (line[n] == "1" and common == 1):
            o2 = line
            o2_tmp.append(line)    
    o2_con =  o2_tmp
    n+=1          
n = 0

while(len(co2_con) > 1): 
    co2_tmp = []
    common, lcommon = most_com(co2_con, n)
    for line in co2_con:
        if(line[n] == "0" and lcommon == 0) or (line[n] == "1" and lcommon == 1):
            co2 = line
            co2_tmp.append(line)           
    co2_con =  co2_tmp
    n+=1
     
print(int(o2, 2) * int(co2, 2))