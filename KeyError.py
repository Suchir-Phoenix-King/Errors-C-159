# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:11:16 2022

@author: PC_RC
"""

dictionary = {"fruit":"mango", "colour":"blue", "bird":"falcon"}

try:
    print(dictionary["animal"])
except(KeyError):
    print("key 'animal' is not present in the dictionary")
