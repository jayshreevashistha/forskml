# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:29:02 2019

@author: computer
"""

import random

names = ['Mary', 'Isla', 'Sam']

secret_names = list(map(lambda x: random.choice(['Mr. Pink',
                                            'Mr. Orange',
                                            'Mr. Blonde']),
                   names))