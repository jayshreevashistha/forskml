# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:58:32 2019

@author: computer
"""

import numpy as np
import matplotlib.pyplot as plt


plt.hist(incomes, 20)
plt.show()

incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
incomes = np.append(incomes, [10000000000])

print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

