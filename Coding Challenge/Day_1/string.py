# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:27:38 2019

@author: computer
"""





# Take name as input from user
name = input("Enter your name with lastname :")

# Find index for space
space_index = name.index(' ')  # or use find function 

print (name[space_index+1:]+' '+name[0:space_index+1])
