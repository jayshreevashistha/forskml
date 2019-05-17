# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:08:09 2019

@author: computer
"""

import re

file = open("simpsons_phone_book.txt")

for line in file:
    if re.search(r'^J.*Neu',line):
        print(line.rstrip())

file.close()
    
    
    
#if re.findall(r'^[J][Neu]$[0-9-]*)
    