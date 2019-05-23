# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:42:18 2019

@author: computer
"""


import numpy as np
Num=input("Enter space separated no.").split()
Num = np.array(Num)

Num=Num.reshape(3,3)

print(Num)
