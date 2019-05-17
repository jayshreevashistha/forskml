# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:42:46 2019

@author: computer
"""

for i in range(1,6):
    print("*"*i)
for j in range(4,0,-1):
    print("*"*j)
    
******************************************

# Enter Number to print pattern
num = int(input("Enter Number to print Pattern: "))

# Prints the upper half of the pattern
for i in range(1,num+1):
    print("*" * i)

# Prints the lower half of the pattern
for i in range(num-1,0,-1):
    print("*" * i)