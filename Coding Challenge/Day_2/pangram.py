# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:09:02 2019

@author: computer
"""


from string import ascii_lowercase as asc_lower

sample=input("write the sentence")
def check(s):
    return set(asc_lower) - set(s.lower())== set([])


if(check(sample)==True):
    print("The string is Pangram")
else:
    print("not pangram")

**************************************************************

# To check if a string is pangram or not
input_string = input("Enter the string :")
count = 0
_list = []
_lower = input_string.lower()
for alpha in _lower:
    _list.append(alpha)

# remove duplicates
final_list = []    

for num in _list: 
 if num not in final_list: 
  final_list.append(num) 
    
for elements in final_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
if count == 26:
    print ("Pangram")
else:
    print ("Not Pangram")