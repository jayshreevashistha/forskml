# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:49:55 2019

@author: computer
"""



def make_bricks(small, big, target):
    if small + big*5 > target:
        return True
    else:
        return False
