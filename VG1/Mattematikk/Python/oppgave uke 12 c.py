# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:01:24 2023

@author: trfaa001
"""

startLønnBirger = 500000
renteBirger = 1.05

startLønnMarte = 520000
renteMarte = 1.5

def f(x):
    return startLønnBirger*renteBirger**x

def g(x):
    return startLønnMarte*renteMarte**x

x = 0

while x <= 5:
    
    skrivfx = "{:.0f}".format(f(x))
    
    print(x, skrivfx)
    x += 1

tjentBirger = f(x) - startLønnBirger
skrivTjentBirger = "{:.0f}".format(tjentBirger)

print("Biger har tjent total ", skrivTjentBirger, "kr i perioden 2015 til og med 2020")

if f(5)-f(4) > g(5)-g(4):
    print("Birger tjente mer enn Marte i 2020")
elif f(5)-f(4) < g(5)-g(4):
    print("Marte tjente mer enn Birger i 2020")
else:
    print("Marte og Birger tjente like mye i 2020")

tjentMarte = g(x)- startLønnMarte
skrivTjentMarte = "{:.0f}".format(tjentMarte)

if tjentBirger > tjentMarte:
    print("I perioden 2015-2020 tjente Birger mer enn Marte")
elif tjentBirger < tjentMarte:
    print("I perioden 2015-2020 tjente Marte mer enn Birger")
else:
    print("I perioden 2015-2020 tjente Birger og Marte like mye")