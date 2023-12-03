# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:20:45 2023

@author: mark.patmore
"""


min_list = []


with open('inputs/day2.txt', 'r') as file:

    for x in file:

        y = x[0:x.index(':')].split(' ')
        
        game_id = int(y[1])
        
        a = x[x.index(':')+1:].split(';')
        
        red_min = 0
        green_min = 0
        blue_min = 0
                
        for i in a:
            split_colors = i.split(',')
            for j in split_colors:
                j = j.strip()
                color_num = int(j[:j.index(' ')])
                if 'red' in j and color_num > red_min:
                    red_min = color_num
                elif 'green' in j and color_num > green_min:
                    green_min = color_num
                elif 'blue' in j and color_num > blue_min:
                    blue_min = color_num
                    
        min_list.append(red_min*green_min*blue_min)
    
print(sum(min_list))    
    