# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:15:40 2022

@author: PC_RC
"""

mylist = [0,1,2,3]
try:
    print(mylist[5])
except IndexError:
    print("index out of range")
