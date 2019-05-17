# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:15:32 2019

@author: computer
"""
"""
inp=input("Enter the string")
d=dict()
for s in inp:
    keys=dict.keys()
    if s in keys:
        d[s] += 1
    else:
        d[s] = 1
        
for key,values in d:
    print(key,values)

"""
# accetping string from user and parsing it into List.
user_input = input("Enter String: ")

character_frequency = {}       # initialising the Dict.

# loop to access every element of the list individually.
for alphabet in user_input:

    # adding every element as a 'key' and its frequency of occurance
    #as 'value' in the Dict.
    character_frequency[alphabet] = character_frequency.get(alphabet,0) + 1
    
print (character_frequency)


########## Pythonic Code ##########
'''
from collections import Counter

print (dict(Counter(user_input)))'''
