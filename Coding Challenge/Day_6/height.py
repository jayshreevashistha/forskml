# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:27:41 2019

@author: computer
"""


people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))

if len(heights) > 0:
    from operator import add
    average_height = reduce(add, heights) / len(heights)