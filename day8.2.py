# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 07:58:42 2023

@author: mark.patmore
"""

from math import lcm


raw_instructions = 'LRLRRRLRLLRRLRLRRRLRLRRLRRLLRLRRLRRLRRRLRRRLRLRRRLRLRRLRRLLRLRLLLLLRLRLRRLLRRRLLLRLLLRRLLLLLRLLLRLRRLRRLRRRLRRRLRRLRRLRRRLRLRLRRLRLRLRLRRLRRRLLRLLRRLRLRRRLRLRRRLRLRRRLRRRLRRLRLLLLRLRRRLRLRRLRLRRLRRLRRLLRRRLLLLLLRLRRRLRRLLRRRLRRLLLRLRLRLRRRLRRLRLRRRLRRLRRRLLRRLRRLLLRRRR'

instructions = raw_instructions * 1000

nodes = {}

with open("inputs/day8.txt", 'r') as file:
    
    for i in file:
        nodes[i[:3]] = i[7:15].split(', ')
    file.close()
    
    
    starting_nodes = []

    for k in nodes.keys():
        if k[2] == 'A':
            starting_nodes.append(k)
    current_nodes = [i for i in starting_nodes]


    count_list = []



    for node in current_nodes:
        current_node = node
        count = 0
        
        for i in instructions:
            if i == 'L':
                current_node = nodes[current_node][0]
            elif i == 'R':
                current_node = nodes[current_node][1]
            count += 1
            if current_node[2] == 'Z':
                break   
            
        count_list.append(count)
        count_tup = tuple(count_list)
            
    a = count_list[0]
    b = count_list[1]
    c = count_list[2]
    d = count_list[3]    
    e = count_list[4]
    f = count_list[5]


    print(lcm(a,b,c,d,e,f))   