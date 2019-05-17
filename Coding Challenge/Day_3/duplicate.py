# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:32:26 2019

@author: computer
"""

# given list
given_list =  [12,24,35,24,88,120,155,88,120,155]

# parsing given list into set to remove duplicate entries
# then again parsing it back to list
output_list = list(set(given_list))

# reversing the new list
output_list.reverse()

print(output_list)