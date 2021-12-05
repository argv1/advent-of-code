#!/usr/bin/env python3
'''
    advent of code 2020 Day 4 Challenge 2
'''

import re

def check_bingo(ticket):
    for col in range(0,5):
        n = 0
        for row in ticket:
            if(sum(1 for value in row.values() if value == True) == 5):
                return calc_res(ticket)
            if list(row.items())[col][1] == True: 
                n+=1
        if n == 5: return calc_res(ticket)

def calc_res(ticket):
    unmarked = 0
    for row in ticket:
        for col in range(0,5):
            if list(row.items())[col][1] == False:
                unmarked += int(list(row.items())[col][0])
    return unmarked      
        
def bingo():
    counter = 1
    for num in drawn_numbers:
        for count, ticket in enumerate(bingo_tickets):            
            for row in ticket:
                if num in row:
                    row[num] = True
                    res = check_bingo(ticket)
                    if(res != None and ticket_no[count] == 0):
                        ticket_no[count] = counter
                        counter+=1
                    if counter == 100:
                        return res*int(num)

with open('K:/OneDrive/Programme/_current/advent-of-code/2021/day4-input.txt', 'r') as f:
    drawn_numbers = f.readline().strip('\n').split(',')
    lines = f.readlines()
n, m = 0, 0
ticket_no = []
bingo_tickets, ticket = [], []
for line in lines[1:]:
    if line == '\n': 
        bingo_tickets.append(ticket)
        ticket = []
        ticket_no.append(0)
        continue
    search =  re.split(r'\s', line.replace('  ', ' ').strip('\n').lstrip(' ')) 
    bingo_line = {
        search[0]: False,
        search[1]: False,
        search[2]: False,
        search[3]: False,
        search[4]: False
    }
    ticket.append(bingo_line)   

print(bingo())