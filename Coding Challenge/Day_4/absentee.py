# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:41:58 2019

@author: computer
"""

file = open('absentee.txt','wt')
max=25
flag=0
while True and max<=25:
    i=input("enter name  ")
    if i ==' ':
        break
    
    file.write(i)
    flag=flag+1
    if flag==max:
        break
file.close()

file = open("absentee.txt","rt")
print(file.readline())

""""""""""""""""""""""""""""""""""""""""""""""""""""""


file = open('absentee.txt','w')
file.close()

with open('absentee.txt','a') as file:
    for i in range(25):
        absent_student_name = input("Enter the absent student name: ")
        if absent_student_name=="":
            break
        file.write(absent_student_name+'\n')
        

file = open('absentee.txt','r')
print file.readlines()
    