# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:05:26 2019

@author: computer
"""

Distance=80
cost_per_litre=80
vehicle_fuel_average=18
cost_of_driving=((1/vehicle_fuel_average)*(Distance)*(cost_per_litre))
print(cost_of_driving)

*************************************************************************

 
# Daily travelling kilometers
travelling_km = float(input("Enter the kilometers you travel in a day: "))
 
# Diesel cost
diesel_cost = 80.0
 
# Vehicle fuel average
vehicle_fuel_avg = 18.0
 
# Fuel you want during travelling
fuel_consumption = (travelling_km/vehicle_fuel_avg)
 
# cost of driving per day to office
cost_per_day = (diesel_cost*fuel_consumption)

print ("Cost of driving per day to office is :"+str(round(cost_per_day,2))+" INR")