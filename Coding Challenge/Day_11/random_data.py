# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:49:04 2019

@author: computer
"""


from collections import Counter

array_of_random_integers = np.random.randint( 5, 15, 40 )

frequency_counter = Counter( array_of_random_integers )

most_frequent_value = frequency_counter.most_common()[0][0]

print ( "The most Frequent Number is",most_frequent_value )




most_frequent_value = np.bincount( array_of_random_integers ).argmax()

print ( "The most Frequent Number is", most_frequent_value )