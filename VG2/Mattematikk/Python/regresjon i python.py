#%%
from pylab import loadtxt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import *

data_original = np.array(loadtxt("Halden.txt", delimiter=" ")) #Gjøre om tekst fil til en array

x_original, y_original = zip(*data_original) #Gjøre om array til to lister

plt.scatter(x_original, y_original) #legg ut punktene fra listen

plt.title(label="Befolkning Halden (år)")

plt.xlabel("år")
plt.ylabel("Befolkningstall")


print("Datasett nedlastet fra SSB:")
plt.show()

data = np.array(loadtxt("Halden_begrenset_område.txt", delimiter=" "))

x_data, y_data = zip(*data)

plt.scatter(x_data, y_data, c="blue")


#def f(t,a,b,c):
#    return a*t+c*math.exp(b*t)

#optimize.curve_fit(f(a, b, c), x, y)

#mymodel = np.poly1d(np.polyfit(x, y, 2))



#myline = np.linspace(1985, 2024)

#plt.plot(myline, mymodel(myline))   


def logRegresjon(x, a, b):
    return a*np.log(x)+b
    #return a*np.log(b*x)+c
    #return a*b**np.log(x)

#parametere = curve_fit(logRegresjon, x, y, maxfev=10000)

popt, pcov = curve_fit(logRegresjon, x_data, y_data, maxfev=10000)


x_fit = np.linspace(1951, 1971, 20)
#y_fit = logRegresjon(x_fit, *parametere)
y_fit = logRegresjon(x_fit, *popt)

plt.plot(x_fit, y_fit, "black")

plt.title(label="Befolkning Halden (år)")

plt.xlabel("år")
plt.ylabel("Befolkningstall")

a, b = zip(popt)


x_fit2 = x_fit
mymodel = np.poly1d(np.polyfit(x_data, y_data, 2))

plt.plot(x_fit2, mymodel(x_fit2), "red")


print("Regresjon med begrenset datasett:")
plt.show()

print("Funksjonen curve fit finner:")
print("a =", a, "b =", b)
print("f(X) = ", a[0], " * ", "lg(x) + ", b[0])
print("f(x) blir ikke brukt, på grunn at den gir et værre resultat enn en lineær regresjon")
# %%
