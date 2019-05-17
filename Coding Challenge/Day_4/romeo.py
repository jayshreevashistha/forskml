# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:48:57 2019

@author: computer
"""

# To open the file
with open("romeo.txt", "rt") as fileobj:

    content = fileobj.readlines()
    
    # List to hold the list of the words
    req_content = []
    for var in content:
        req_content.append(var.split())
    
    # To count the words using dictionary
    dict1 = {}
    for var2 in req_content:
        for var3 in var2:
            if var3 not in dict1:
                dict1[var3] = 1
            else:
                dict1[var3]+=1
            
        