# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:21:06 2022

@author: trfaa001
"""


print("Programmet skal løse andregradslikningen ")
print("ax^2 + bx = 0 ved hjelp av abc-formelen.")
print("Skriv inn verdien for a, b og c.")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b**2 - 4*a*c

x1 = (-b + d**-1)/(2*a)
x2 = (-b - d**-1)/(2*a)

print("Løsningen på andregradslikningen er:")
print("x1 = ", x1, "x2 = ", x2)