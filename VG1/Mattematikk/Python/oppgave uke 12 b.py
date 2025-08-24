# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:53:46 2023

@author: trfaa001
"""

startLønnBirger = 500000
renteBirger = 1.05

def f(x):
    return startLønnBirger*renteBirger**x

x = 0

while x <= 5:
    
    skrivfx = "{:.0f}".format(f(x))
    
    print(x, skrivfx)
    x += 1

tjentBirger = f(x) - startLønnBirger
skrivTjentBirger = "{:.0f}".format(tjentBirger)

print("Biger har tjent total ", skrivTjentBirger, "kr i perioden 2015 til og med 2020")