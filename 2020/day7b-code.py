#!/usr/bin/env python3
'''
    advent of code 2020 Day 7 Challenge 2
'''

def get_bags_count(lines, bag_color):
    res = 0
    for line in lines:
        outer_bag, inner_bags = line.split('contain ')
        outer_bag_color = outer_bag.split(' bags')[0]
        if bag_color == outer_bag_color and 'no other bags' not in inner_bags:
            inner_bags_list = inner_bags.split(', ')
            res = sum([int(x.split(' ')[0]) for x in inner_bags_list])
            for inner_bag in inner_bags_list:
                bag_count = int(inner_bag.split(' ')[0])
                inner_bag_color = inner_bag.split(' bag')[0][2:]
                res += bag_count * get_bags_count(lines, inner_bag_color)
    return res

def main():
    bag_color, path = 'shiny gold', 'H:/OneDrive/Programme/_current/adventofcode/2020/day7-input.txt'
    with open(path, 'r') as f:  
        lines = f.read().splitlines()
        print(get_bags_count(lines, 'shiny gold'))
    
if __name__ == '__main__':
    main()