# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:14:37 2019

@author: computer
"""

sample = input("enter numbers: ").split()
all_pos=True
palindrome=False

for i in sample:
    if int(i)<0:
        all_pos = False
    
if all_pos:
    for i in sample:
        if i == i[::-1]:
            palindrome = True


if palindrome:
    print("palindrome")
else:
    print("not palindrome")
    
    ***************************************
    
    user_input = input("Enter space seperated values :").split()

input_length  = len(user_input)
count = 0
pallindromic_integer = False

for num in user_input:
    if int(num) > 0:
        count += 1

if count == input_length:
    for positive_num in user_input:
        if positive_num == positive_num[::-1]:
            pallindromic_integer = True

print(pallindromic_integer)


****************************************************************

# Short Logic using the all and any keyword

# give list of inputs from user
user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    
