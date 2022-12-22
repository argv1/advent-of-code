#!/usr/bin/env python3
'''
    advent of code 2022 Day 5
'''

import re

def split_input():
    tmp, tmp_input_v, input_v, tmp_commands, commands = [],[], [], [], []
    with open(r"H:/OneDrive/Programme/_current/advent-of-code/2022/day5-input.txt", "r") as f: 
        for entry in f.readlines():
            if entry.startswith('['):
                tmp_input_v.append(entry.strip('\n'))
            elif entry.startswith('move'):
                tmp_commands.append(entry.strip('\n'))
        
    for m in range(1,tmp_input_v[-1].count("[")*4,4):
        for n in reversed(range(len(tmp_input_v))):
            if tmp_input_v[n][m] != " ":
                tmp.append(tmp_input_v[n][m])
        input_v.append(tmp)
        tmp = []        

    pattern = "^move (\d+) from (\d+) to (\d+)$"
    for line in tmp_commands:
        result = re.search(pattern, line)
        tmp = [result.groups()[0], result.groups()[1], result.groups()[2]]
        commands.append(tmp)    
    
    return input_v, commands


def solver(input_v, commands):
    result_sol_a, result_sol_b, input_v_sol_b = "", "", input_v.copy()
     
    for comm in commands:
        for _ in range(0, int(comm[0])):
            input_v[int(comm[2])-1].append(input_v[int(comm[1])-1].pop())
            
    for comm in commands:
        input_v_sol_b[int(comm[2])-1].extend(input_v_sol_b[int(comm[1])-1][-int(comm[0]):])
        input_v_sol_b[int(comm[1])-1] = input_v_sol_b[int(comm[1])-1][:(len(input_v_sol_b[int(comm[1])-1])-int(comm[0]))]   
       
    for n in range(0,len(input_v)):
        result_sol_a += input_v[n][-1]
        result_sol_b += input_v_sol_b[n][-1]
    print(f"Solution A: {result_sol_a}\nSolution B: {result_sol_b}") 
    
def main():
    input_v, commands = split_input()
    solver(input_v, commands)
    
if __name__  == "__main__":
    main()
