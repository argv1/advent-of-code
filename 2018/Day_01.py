#!/usr/bin/env python3

'''
    advent of code 2018 Day 1
'''

def main():
    result_a = 0
    result_b = None
    tmp = 0
    frequencies = set()

    with open(r"d:/AOC/2018/Day_01_Input.txt", "r") as f:
        for line in f:
            result_a += int(line)

        while result_b is None:
            f.seek(0) 
            for line in f:
                tmp += int(line)

                if tmp in frequencies:
                    result_b = tmp
                    break
                frequencies.add(tmp)


    print(f"{result_a = }\n{result_b = }")

if __name__  == "__main__":
    main()