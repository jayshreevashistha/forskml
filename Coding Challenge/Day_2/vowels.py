# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:42:41 2019

@author: computer
"""

state_name=['Alabama','California','Oklohoma','Florida']
vowel=['a','e','i','o','u','A','E','I','O','U']
final_list=[]
for words in state_name:
    word=list(word)
    for letter in vowel:
        if letter in word:
            word.remove(letter)
            

print(final_list)

*****************************************************************



state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list('aeiou')

final_list = []

for state in state_name:
    state_elements = list(state.lower())
    
    for element in vowels:
        while element in state_elements:
            state_elements.remove(element)
    final_list.append("".join(state_elements))

print (final_list)


    

    
        