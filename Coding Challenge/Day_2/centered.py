# -*- coding: utf-8 -*-
"""
Created on Thu May  9 06:36:28 2019

@author: computer
"""
def centered_average(nums):
  items = len(nums)
  total = 0
  high = max(nums)
  low = min(nums)
  for num in nums:
    total += num
  avg = (total -high-low) / (items-2)
  return avg