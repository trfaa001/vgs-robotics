# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:38:28 2023

@author: trfaa001
"""

x1 = float(input("Hva er x i det første punktet?: "))
x2 = float(input("Hva er x i det andre punktet?: "))
y1 = float(input("Hva er y i det første punktet?: "))
y2 = float(input("Hva er y i det andre punktet?: "))

a = (y2-y1)/(x2-x1)
b = y2-a*x2

print("Funskjonen er: f(x) = ", a,"x + ", b)