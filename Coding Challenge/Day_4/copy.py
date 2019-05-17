# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:45:43 2019

@author: computer
"""

with open("new.txt", "rt") as file1:
    with open("copy.txt","wt") as file2:
        for line in file1:
            file2.write(line)
        content = file1.readline()
    print(content)
    

    
