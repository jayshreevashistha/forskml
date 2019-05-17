# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:38:33 2019

@author: computer
"""

import re
while True:
    inp=input("Enter credit card number ").split("<")
    if not inp:
        break
    for val in inp:
        if re.findall(r'^[4-6][0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}',val):
            print("valid")
        else:
            print("invalid")