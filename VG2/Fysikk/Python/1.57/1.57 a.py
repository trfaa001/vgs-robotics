# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:45:49 2023

@author: trfaa001
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    posisjon = 8*x+1/2*-9.81*x**2
    return posisjon

x_verdier = np.linspace(-5, 5, 100)
y_verdier = f(x_verdier)

plt.plot(x_verdier, y_verdier)
print("Posisjon på 1,2s", f(1.2))
