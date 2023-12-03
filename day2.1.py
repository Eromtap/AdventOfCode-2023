# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:45:38 2023

@author: mark.patmore
"""
RED = 12
GREEN = 13
BLUE = 14



game_id_list = []


with open('inputs/day2.txt', 'r') as file:

    for x in file:

        y = x[0:x.index(':')].split(' ')
        
        game_id = int(y[1])
        
        a = x[x.index(':')+1:].split(';')
        
        possible = True
        
        for i in a:
            split_colors = i.split(',')
            for j in split_colors:
                j = j.strip()
                color_num = int(j[:j.index(' ')])
                if 'red' in j and color_num > RED:
                    possible = False
                    break
                elif 'green' in j and color_num > GREEN:
                    possible = False
                    break
                elif 'blue' in j and color_num > BLUE:
                    possible = False
                    break
            if possible == False:
                break
        if possible == True:
            game_id_list.append(game_id)
            
print(sum(game_id_list))            