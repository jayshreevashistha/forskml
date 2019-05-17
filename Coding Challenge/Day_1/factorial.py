# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:46:27 2019

@author: computer
"""


from math import factorial

input_number = input("Enter the number >")
Factorial_of_input_number = factorial(int(input_number))
print ("Factorial of {0} is {1}".format(input_number,Factorial_of_input_number))