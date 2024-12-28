#!/usr/bin/env python3

'''
    advent of code 2017 Day 2
'''

def main():
    result_a, result_b = 0, 0

    with open(r"d:/AOC/2017/Day_02_Input.txt", "r") as f:
        for line in f:
            line = line.strip().split("\t")
            line = [ int(x) for x in line]
            line.sort()
            result_a += (line[-1] - line[0])
            
            for n in range(len(line)):
                c+=1
                found = False
                for m in range(len(line)):
                    if line[m] % line[n] == 0 and line[m] / line[n] != 1:
                        result_b += line[m] / line[n]
                        found = True
                        break
                if found:
                    break
       
    print(f"{result_a = }\n{result_b = }")

if __name__  == "__main__":
    main()