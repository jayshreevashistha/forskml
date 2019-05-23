# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:08:08 2019

@author: computer
"""

import mysql.connector
import pandas as pd
from selenium import webdriver
driver = webdriver.Firefox(executable_path='C:/Users/computer/Downloads/geckodriver-v0.24.0-win32(1)/geckodriver.exe')
url="https://bidplus.gem.gov.in/bidlists"
driver.get(url)

conn = mysql.connector.connect(user='root',password='',hoost='localhost')

c=conn.cursor()

A=[]
BID_NO=[]
items=[]
Quantity_Required=[]
Department_Name_address=[]
Start_date=[]
end_time=[]
end_date=[]

