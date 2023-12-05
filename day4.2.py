# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:42:39 2023

@author: mark.patmore
"""



y = []


total_cards = {'0':1}
added = 0
iterations = 0

with open('inputs/day4.txt') as x:
    for iteration, i in enumerate(x):
        if str(iteration+1) not in total_cards:
            total_cards[str(iteration+1)] = 0
        for dups in range(total_cards[str(iteration)]+added):
            card_score = 0
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
                    card_score += 1
            iterations += 1
                    
            if card_score > 0:
                for m in range(1, card_score + 1):
                    if str(iteration+m) in total_cards:
                        total_cards[str(iteration+m)] += 1 
                    else:
                        total_cards[str(iteration+m)] = 1

        added = 1
        
print(iterations) 