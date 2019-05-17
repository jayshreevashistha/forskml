# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:14:54 2019

@author: computer
"""

import os
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'student.db' )
c = conn.cursor()

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

df = DataFrame(c.fetchall())  
df.columns = ["Name","Age","Roll_no","Branch"]

conn.commit()
conn.close()
