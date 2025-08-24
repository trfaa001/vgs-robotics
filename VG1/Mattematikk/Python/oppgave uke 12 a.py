# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:42:45 2023

@author: trfaa001
"""

def f(x):
    return 500000*1.025**x

x = 0

while x <= 5:
    
    skrivfx = "{:.0f}".format(f(x))
    
    print(x, skrivfx)
    x += 1