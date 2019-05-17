# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:48:07 2019

@author: computer
"""

import mysql.connector 
conn = mysql.connector.connect(user='jayshree',password='astrology1',
                               host='db4free.net',database ='project_123')

c = conn.cursor()

c.execute("DROP Table students;")

c.execute ("""CREATE TABLE students(
          Name  TEXT,
          Age Integer,
          Roll_no Integer,
          Branch Text
          )""")

c.execute("INSERT INTO students VALUES ('Jaya',20, 1,'IT')")
c.execute("INSERT INTO students VALUES ('Jayshree',19,2,'CSE')")
c.execute("INSERT INTO students VALUES ('Nisha',18,3,'ECE')")
c.execute("INSERT INTO students VALUES ('Rishi',21,4,'ME')")
c.execute("INSERT INTO students VALUES ('Aksh',19,5,'IT')")

c.execute("SELECT * FROM students")

from pandas import DataFrame
df = DataFrame(c.fetchall())  

#!pip install mysql-connector-python