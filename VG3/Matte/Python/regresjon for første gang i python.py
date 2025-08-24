from scipy.optimize import curve_fit
from pylab import plot, linspace, sin, loadtxt, exp
import matplotlib.pyplot as plt

x = [1, 3, 4, 5, 7, 8, 10, 12, 13, 15, 16, 17]
y = [40, 30, 35, 60, 80, 90, 110, 120, 140, 170, 200, 210]

def f(t, a, b, c, d):
    return a*exp(b*t) + c + d*t

[a, b, c, d] = curve_fit(f, x, y)[0] # Den nulte skal være variabelen

print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

plot(x, y, "o")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
t = linspace(min(x), max(x), 1000)
plot(t, f(t, a, b, c, d), "r")
plt.show()

