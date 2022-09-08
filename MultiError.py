# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:19:17 2022

@author: PC_RC
"""

from tkinter import *

root = Tk()
root.geometry("600x400")


list_name = ["Elsa", "Anna", "Kristoff", "Sven", "Olaf"]
dict_student = {"name":"Antaeus", "age":"12"}


try:
    print(list_name[6])
    print(dict_student["mom"])
    
    
except IndexError:
    print("Error","This index does not exist")
except KeyError:
    print("Error","This key does not exist")
    

root.mainloop()