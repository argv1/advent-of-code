#!/usr/bin/env python3

'''
    advent of code 2017 Day 1
'''

def main():
    
    result_a, result_b = 0, 0

    with open(r"d:/AOC/2017/Day_01_Input.txt", "r") as f:
        for line in f:
            line = line.strip()
            steps = int(len(line) / 2)

            for n in range(len(line)):
                if line[n] == line[n-1]:
                    result_a += int(line[n])                  
                
                if line[n] == line[n - steps]:
                    result_b += int(line[n])   
       
    print(f"{result_a = }\n{result_b = }")

if __name__  == "__main__":
    main()