# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 07:27:30 2023

@author: mark.patmore
"""

raw_instructions = 'LRLRRRLRLLRRLRLRRRLRLRRLRRLLRLRRLRRLRRRLRRRLRLRRRLRLRRLRRLLRLRLLLLLRLRLRRLLRRRLLLRLLLRRLLLLLRLLLRLRRLRRLRRRLRRRLRRLRRLRRRLRLRLRRLRLRLRLRRLRRRLLRLLRRLRLRRRLRLRRRLRLRRRLRRRLRRLRLLLLRLRRRLRLRRLRLRRLRRLRRLLRRRLLLLLLRLRRRLRRLLRRRLRRLLLRLRLRLRRRLRRLRLRRRLRRLRRRLLRRLRRLLLRRRR'

instructions = raw_instructions * 100

nodes = {}
starting_node = 'AAA' 

with open("inputs/day8.txt", 'r') as file:
    
    for i in file:
        nodes[i[:3]] = i[7:15].split(', ')
    file.close()


current_node = starting_node
count = 0
for i in instructions:
    if i == 'L':
        current_node = nodes[current_node][0]
    elif i == 'R':
        current_node = nodes[current_node][1]
    count += 1
    if current_node == 'ZZZ':
        break                



print(count)









