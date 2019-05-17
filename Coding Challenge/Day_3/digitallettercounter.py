# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:30:36 2019

@author: computer
"""

from collections import OrderedDict 
# accepting input from user, expected input to be combionation of
#lettters and numbers.
user_input = input("Enter string : ")

# initialising the counter for letter and digit
dict1 = OrderedDict() 
dict1["Digits"] = 0
dict1["Letters"] = 0


# loop to access every element of string individually.
for character in user_input:    
    if character.isalpha():    # conditionto check for Letter.
        # if found increase counter variable by 1.
        dict1["Letters"] = dict1["Letters"] + 1 
    elif character.isdigit():      # conditiion to check for digit.
        # if found increase counter variable by 1.       
        dict1["Digits"] = dict1["Digits"] + 1 
            
for key, value in dict1.items() :
  print ( key, value )