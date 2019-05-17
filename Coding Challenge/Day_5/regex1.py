# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:44:55 2019

@author: computer
"""

import re

while True:
    li1=input("enter no").split(">")
    if not li1:
        break

    for val in li1:
        if re.findall(r'[+-.]?[0-9]\.[0-9]*',val):
            print("True")
        else:
            print("False")