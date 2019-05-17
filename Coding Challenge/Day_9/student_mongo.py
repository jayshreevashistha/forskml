# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:26:06 2019

@author: computer
"""

import pymongo

client = pymongo.MongoClient("mongodb://Jayshree:astrology%40123@cluster0-shard-00-00-w2mmd.mongodb.net:27017,cluster0-shard-00-01-w2mmd.mongodb.net:27017,cluster0-shard-00-02-w2mmd.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.project123
def add_student(Name,Age,Roll_no,Branch):
    mydb.Project.insert_one(
            {
             "Name": Name,
             "Age": Age,
             "Roll_no": Roll_no,
             "Branch": Branch
             })
    return "student added successfully"
def fetch_all_student():
    user = mydb.Project.find()
    for i in user:
        print(i)
        
add_student('Jaya',20,1,'IT')
add_student('Jayshree',19,2,'CSE')
add_student('Nisha',18,3,'ECE')

fetch_all_student()
        

