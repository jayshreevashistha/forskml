# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:31:52 2019

@author: computer
"""

days= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

inp=input("Enter the days").split(",")

final_list=[]

for item in days:
    if item not in inp:
        index=days.index(item)
        final_list.insert(index,item)
    if item in inp:
        index=days.index(item)
        final_list.insert(index,item)
        
print(tuple(final_list))

""""""""""""""""""""""""""""""""""""""""""""''
given_tuple = ('Monday', 'Wednesday', 'Thursday', 'Saturday')

new_tuple = (given_tuple[0],) + ('Tuesday',) + given_tuple[1:3] + ('Friday',) + (given_tuple[-1],) + ('Sunday',)

print (new_tuple)
