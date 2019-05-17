# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:19:30 2019

@author: computer
"""

sample=input("Enter the numbers").split(",")

print("list:",list(sample))
print("tuple:",tuple(sample))


""""""""""""""""""""""""""""""""""""""""""""""""
# Enter comma separated numbers
user_list = input("Enter comma seperated numbers :").split(",")
new_list = []

for i in user_list:
    new_list.append(int(i))
    
# list to tuple conversion
user_tuple = tuple(user_list)

print ("List : "+str(user_list))
print ("Tuple : "+str(user_tuple))

""""""""""""""""""""""""""""""""""""""""""""""""""