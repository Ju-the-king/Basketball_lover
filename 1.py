# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:02:52 2023

@author: abroc
"""

#%% Open and read file content

file = open("input.txt","r")
content = file.readlines()


#%% Part 1

somme = []

for elem in content :
    
    sequence = ""
    
    for el in elem :
        
        if el in [str(i) for i in range(10)] :
            
            sequence += el
            
    somme.append(int(sequence[0]+sequence[-1]))     
    
seum = sum(somme)
                 
#%% Part 2

somme2 = []
numbers = ["one","two","three","four","five","six","seven","eight","nine"]
numbers_r = ["eno","owt","eerht","ruof","evif","xis","neves","thgie","enin"]

for elem in content :
    
    sequence = ""

    new_elem = elem
    
    for num in numbers :
        
        if num in new_elem :
        
            index = new_elem.index(num)        
            new_elem = new_elem[:index] + num[0] + str(numbers.index(num)+1) + new_elem[index:]
        
        if num[::-1] in new_elem[::-1] :
        
            index = new_elem[::-1].index(num[::-1])        
            new_elem = new_elem[::-1][:index] + num[::-1] + str(numbers_r.index(num[::-1])+1) + new_elem[::-1][index:]
            new_elem = new_elem[::-1]
                        
    for el in new_elem :
        
        if el in [str(i) for i in range(10)] :
            
            sequence += el 
    
    somme2.append(int(sequence[0]+sequence[-1]))
    
    print(new_elem, elem, somme2[-1])
    
seum2 = sum(somme2)

