#%%
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    akselerasjon = 0.5*x+8
    return akselerasjon

def g(x):
    fart = f(x)*x
    return fart

def h(x):
    posisjon = 1/2*f(x)*x**2
    return posisjon

xAkselerasjon = np.arange(0, 10, 1)
yAkselerasjon = f(xAkselerasjon)

plt.plot(xAkselerasjon, yAkselerasjon)

xFart = np.arange(0, 10, 1)
yFart = g(xFart)

plt.plot(xFart, yFart)

xPosisjon = np.arange(0, 10, 1)
yPosisjon = h(xPosisjon)

plt.plot(xPosisjon, yPosisjon)
# %%
