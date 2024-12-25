#!/usr/bin/env python3

'''
    advent of code 2019 Day 1
'''

def main():
    
    result_a, result_b = 0, 0

    with open(r"d:/AOC/2019/Day_01_Input.txt", "r") as f:
        for line in f:
            fuel = (int( int(line) / 3) - 2)
            result_a += fuel
            result_b += fuel

            while fuel > 6:
                fuel = (int( int(fuel) / 3) - 2)
                result_b += fuel

    print(f"{result_a = }\n{result_b = }")

if __name__  == "__main__":
    main()