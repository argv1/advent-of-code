#!/usr/bin/env python3

'''
    advent of code 2017 Day 2
'''

from itertools import permutations

def main():
    result_a, result_b = 0, 0

    with open(r"d:/AOC/2017/Day_02_Input.txt", "r") as f:
        for line in f:
            c+=1
            line = list(map(int, line.strip().split("\t")))
            result_a += max(line) - min(line)
            
            for a, b in permutations(line, 2):
                if a % b == 0:
                    result_b += a // b
                    break
       
    print(f"{result_a = }\n{result_b = }")

if __name__  == "__main__":
    main()
