# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:22:38 2023

@author: mark.patmore
"""

''' simple solution to day1 (year 2023). first, replace the spelled out numbers with 
their integer counterparts. Then run through each one and add numerical values 
to a list. Concat the first and last values of each list and append them to 
the final list. Lastly, just sum the final list. I didn't separate first and 
second challenge here, so this is number 2. Maybe I will tomorrow. Also, its a 
code challenge, so I don't care about variable names lol.
'''

num_list = []

with open("day1.txt", "r") as file:
    for x in file:   

        for i in range(len(x)):
            if x[i:i+3] == 'one':
                x = x.replace('one', '1', 1)
            elif x[i:i+3] == 'two':
                x = x.replace('two', '2', 1)
            elif x[i:i+5] == 'three':
                x = x.replace('three', '3', 1)
            elif x[i:i+4] == 'four':
                x = x.replace('four', '4', 1)        
            elif x[i:i+4] == 'five':
                x = x.replace('five', '5', 1)  
            elif x[i:i+3] == 'six':
                x = x.replace('six', '6', 1)        
            elif x[i:i+5] == 'seven':
                x = x.replace('seven', '7', 1)   
            elif x[i:i+5] == 'eight':
                x = x.replace('eight', '8', 1)   
            elif x[i:i+4] == 'nine':
                x = x.replace('nine', '9', 1)            
        y = []
        for i in x:
            if i.isnumeric():
                y.append(i)
        num_string = y[0] + y[-1]
    
        num_list.append(int(num_string))



print(sum(num_list))
