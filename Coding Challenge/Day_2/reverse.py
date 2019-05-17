# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:44:16 2019

@author: computer
"""

def reverse(inputString):
    
    stringLength = int(len(inputString))
    reversedString = ""
    for i in range(0,stringLength):
        reversedString = reversedString+inputString[-i-1]
    print (str(reversedString))
 
 
stringToReverse = input("Enter the string to reverse")
 
reverse(stringToReverse)