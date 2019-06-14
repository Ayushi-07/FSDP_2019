# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:14:29 2019

@author: Ayushi Agrawal
"""

#n reverse order with a space between them, 
    #find the index using find/index function and then print using slicing concept of the index
       
    
    #Sylvester Fernandes
       

name = input("enter your name with lastname> ")
space_index = name.find(" ")
final_output = name[space_index + 1:] + ' ' +  name[:space_index + 1]
print(final_output)