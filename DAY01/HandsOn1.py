# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:22:47 2019

@author: Ayushi Agrawal
"""

#HandsOn1

number = 1
while(number <= 10):
    print(number)
    number += 1
    
#HandsOn2

number = 1
while True:
    print(number)
    number += 1
    if(number > 10):
        break
        
#HandsOn3
        
number = 1
while(number <= 10):
    if(number % 2 == 0):
        print(number)
    number += 1    
    
#HandsOn4

number = 1
while True:
    if(number % 2 == 0):
        print(number)
    number += 1
    if(number == 10):
        break
    
#HandsOn5
        
number = 1 
while(number <= 10):
    if(number % 2 != 0):
        print(number)
    number += 1
    
#HandsOn6

number = 1
while True:
    if(number % 2 != 0):
        print(number)
    number += 1
    if(number == 10):
        break
    