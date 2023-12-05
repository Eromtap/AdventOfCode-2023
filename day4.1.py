# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:37:07 2023

@author: mark.patmore
"""

with open('inputs/day4.txt', 'r') as x:
    


    total_score = 0
    card_score = 0
    
    for i in x:
        winning_numbers = []
        winning_string = i[i.index(':'):i.index('|')-1].split(' ')
        for j in winning_string:
            if j.isnumeric():
                winning_numbers.append(int(j))
            
        player_numbers = []
        player_string = i[i.index('|')+1:].split(' ')
        for k in player_string:
            k = k.strip('\n')
            if k.isnumeric():
                player_numbers.append(int(k))
                    
        for l in player_numbers:
            if l in winning_numbers:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        total_score += card_score
        card_score = 0
        
    print(total_score)    