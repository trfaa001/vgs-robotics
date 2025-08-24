# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:20:50 2022

@author: trfaa001
"""

a = int(input("Hvor lang er den lengste siden?"))
b = int(input("Hvor lang er den andre siden?"))
c = int(input("Hvor lang er den tredje siden?"))

if a**2 == b**2+c**2:
    print("Trekanten er rettvinklet")
else:
    print("Trekanten er ikke rettvinklet")
