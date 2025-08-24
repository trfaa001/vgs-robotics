# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:15:52 2023

@author: trfaa001
"""

s = 0
v = 0
t = 0
dt = 0.01
t_slutt = 5

while t < t_slutt:
    a = 1*dt
    v = v + a*t
    s = s + v*dt
    t = t + dt
print("På", t_slutt, "s har gjenstanden beveget seg", s, "m")