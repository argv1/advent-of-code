#!/usr/bin/env python3
'''
    advent of code 2020 Day 5 Challenge 2
'''

ids, row, path = [], [64,32,16,8,4,2,1,4,2,1], 'H:/OneDrive/Programme/_current/adventofcode/2020/day5-input.txt'
with open(path, 'r') as f:  
    for line in f.readlines():
        row_nb, seat_nb = 0, 0
        for idx, entry in enumerate(line):
            if(line[idx] == "B"):
                row_nb+= row[idx]
            elif(line[idx] == "R"):
                seat_nb+= row[idx]
        
        ids.append(row_nb * 8 + seat_nb)

ids.sort()
for entry in range(1,len(ids)-1):
    if(ids[entry] -1 != ids[entry-1] and ids[entry] +1 == ids[entry+1]):
        print(int((ids[entry-1]+(ids[entry]))/2))