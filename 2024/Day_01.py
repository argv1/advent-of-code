#!/usr/bin/env python3

'''
    advent of code 2024 Day 1
'''

def main():
    tmp, a, b = [], [], []
    result_task_a, result_task_b  = 0, 0

    with open(r"E:/AOC/2024/Day_01_Input.txt", "r") as f:
        for line in f:
            tmp = line.split("   ")
            a.append(int(tmp.pop(0)))
            b.append(int(tmp.pop().strip()))

    a.sort()
    b.sort()

    for n in range(0,len(a)):
        result_task_a += abs(a[n] - b[n])
        result_task_b += ( a[n] * b.count(a[n]) )

    print(f"{result_task_a = }\n{result_task_b = }")

if __name__  == "__main__":
    main()