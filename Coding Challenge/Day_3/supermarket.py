# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:21:14 2019

@author: computer
"""

from collections import OrderedDict
od=OrderedDict()

while True:
    inp=input(" > ")
    
    if not inp:
        break
    l=inp.split()
    key,value=l[:-1],int(l[-1])
    key=" ".join(key)
       
        
    od[key]= od.get(key,0) + value

print(od)    


for key,item in od.items():
    print(key,item)
    
""""""""""""""""""""""""""""""""""""""""""""""""
from collections import OrderedDict


# make Object of OrderDict
od = OrderedDict()

while True:
    # take items from user as input
    user_input = input("Enter item with price : ")

    if not user_input:
        break
    
    # use split function to get item's price value
    temp = user_input.split()
    price = temp[-1]
    
    # join rest string which is item name
    item = " ".join(temp[:-1])
    
    # Adding and updating price of the item using orderdict function 
    od[item] = od.get(item,0) + int(price)

for k,v in od.items():
    print (k,v)
    
    
    
    
    
    
    
    






