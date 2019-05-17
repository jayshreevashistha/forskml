# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:06:21 2019

@author: computer
"""

import random

guesstaken=0
number=random.randrange(1,10)
print("guess the secret number from 1 to 10")

while guesstaken<6:
    print("Take a guess")
    guess=input()
    guess=int(guess)
    
    guesstaken=guesstaken+1
    
    if guess<number:
        print("your guess is too low")
    
    elif (guess>number):
        print("your guess is too high")
        
    else:
        break
    
if guess==number:
    guesstaken=str(guesstaken)
    print("guess is right")
    
if guess!=number:
    number=str(number)
    print("guess is not right,no was"+number)