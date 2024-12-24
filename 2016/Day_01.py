#!/usr/bin/env python3

'''
    advent of code 2016 Day 1
'''

def main():
    
    grid = [0,0]
    directions = ["N", "E", "S", "W"]
    current_direction, x, y = 0, 0, 0
    visited_positions = set()
    first_revisited = None

    direction_offsets = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0)
    }

    with open(r"d:/AOC/2016/Day_01_Input.txt", "r") as f:
        for line in f:
            coordinates = line.split(", ")

    for element in coordinates:
        direction = element[0]
        blocks = int(element[1:])

        if direction == "R":
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4

        current_dir = directions[current_direction]

        for _ in range(blocks):
            dx, dy = direction_offsets[current_dir]
            x += dx
            y += dy

            if (x, y) in visited_positions and first_revisited is None:
                first_revisited = (x, y)
            visited_positions.add((x, y))

    print(f"Result a: {abs(x) + abs(y) = }\nResult b: {abs(first_revisited[0]) + abs(first_revisited[1]) = }")

if __name__  == "__main__":
    main()