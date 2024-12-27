#!/usr/bin/env python3

'''
    advent of code 2015 Day 2
'''

def main():
    
    result_a, result_b = 0, 0

    with open(r"d:/AOC/2015/Day_02_Input.txt", "r") as f:
        for line in f:
            line = line.strip('\n').split("x")
            line = [ int(x) for x in line]
            line.sort()
            result_a += (line[0] * line[1] * 2) + (line[0] * line[2] * 2) + (line[1] * line[2] * 2) + (line[0] * line[1] )
            result_b += (line[0] *2) + (line[1] * 2) + (line[0] * line[1] * line[2]) 

    print(f"{result_a = }\n{result_b = }")

if __name__  == "__main__":
    main()