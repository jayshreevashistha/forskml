# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:27:53 2019

@author: computer
"""



user_input = input("Enter comma seperated nos >").split(",")

previous_number_is_13 = False
total = 0

for number in user_input:
    if int(number) == 13:
        previous_number_is_13 = True
    
    elif not previous_number_is_13:
        total += int(number)
    
    elif previous_number_is_13 and int(number) != 13:
        previous_number_is_13 = False

print (total)


############################################
##            Another way                 ##
############################################

'''
total = 0

for index in range( len( list_of_integers ) ):
    # checks if current number or previous number is 13
    if (list_of_integers[index] == 13 or list_of_integers[index-1] == 13):
        continue
    total += 1

print (total)
'''