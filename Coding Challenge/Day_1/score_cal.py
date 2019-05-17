# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:13:49 2019

@author: computer
"""

A1=int(input())
A2=int(input())
A3=int(input())
E1=int(input())
E2=int(input())
weighted_score=(A1+A2+A3)*0.1+(E1+E2)*0.35
print(weighted_score)



# Enter marks for assignments 
a1 = int(input("Enter Marks for Assignment 1: "))
a2 = int(input("Enter Marks for Assignment 2: "))
a3 = int(input("Enter Marks for Assignment 3: "))

# Enter marks for exams
e1 = int(input("Enter Marks for Exam 1: "))
e2 = int(input("Enter Marks for Exam 2: "))

# Calculating weighted_score
weighted_score = ( a1 + a2 + a3 ) * 0.1 + (e1 + e2 ) *  0.35

print("Weighted Score is " + str(weighted_score))