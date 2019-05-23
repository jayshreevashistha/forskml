# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:31:14 2019

@author: computer
"""

import numpy as np
                          
incomes = np.random.normal(150, 20, 1000)

import matplotlib.pyplot as plt
plt.hist(incomes, 40)
plt.show()


print("Standard Deviation is: ", np.std(incomes))
print("variance is: ",np.var(incomes))