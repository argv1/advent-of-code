#!/usr/bin/env python3

'''
    advent of code 2015 Day 1
'''

def main():
    
    n, floor = 1, 0

    with open(r"d:/AOC/2015/Day_01_Input.txt", "r") as f:
        for line in f:
            a = line.count("(")
            b = line.count(")")
            print(f"{a - b = }")
            for e in line:
                if e == "(":
                    floor += 1
                else:
                    floor -= 1
                if floor < 0:
                    print(f"{n = }")
                    break
                n += 1

if __name__  == "__main__":
    main()