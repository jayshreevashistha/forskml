# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:01:23 2019

@author: computer
"""

import re
inp=input("enter email").split(">")
for val in inp:
    if re.findall(r'[a-z0-9-_]?@[a-z]*\.[a-z]{2,4}',val):
        print(val)
    else:
        print("not valid")

