# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:19:58 2023

@author: mark.patmore
"""

''' I cheated and just put the input in this one cause it was so small lol '''


time = [35937366]
distance = [212206012011044]

ways_to_win = []

for iteration, i in enumerate(time):
    count = 0
    travel_time = 1
    hold_time = i - 1
    while hold_time > 0:
        if hold_time * travel_time > distance[iteration]:
            count += 1
        hold_time -= 1
        travel_time += 1
    
    ways_to_win.append(count)

multiply = 1
for i in ways_to_win:
    multiply *= i
    
print(multiply)