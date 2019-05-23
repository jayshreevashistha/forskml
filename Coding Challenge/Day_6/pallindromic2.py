# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:30:04 2019

@author: computer
"""

user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")