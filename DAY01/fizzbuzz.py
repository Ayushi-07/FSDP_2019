# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:28:21 2019

@author: Ayushi Agrawal
"""

count = 1
while (count <= 100):
    if(count % 3 == 0 and count % 5 == 0):
        print("fizzbuzz")
    elif(count % 3 == 0 ):
        print("fizz")
    elif(count % 5 == 0):
        print("buzz")
    else:
        print(count)
    count += 1    
    
    
