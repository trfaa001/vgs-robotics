#%%

from pylab import *

def f(x):
    akselerasjon = 0.5*x+8
    return akselerasjon



x_verdier = linspace(0, 10, 100)
y_verdier = f(x_verdier)

plot(x_verdier, y_verdier)
show()
