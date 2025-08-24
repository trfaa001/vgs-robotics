#%%
from pylab import loadtxt
import matplotlib.pyplot as plt

data = loadtxt("rakett.txt", delimiter="\t", usecols = (0,1), skiprows=1) #Gjøre om tekst fil til en array
x = data[:, 0]
y = data[:, 1]

Areal = 0
n=0

while n < 39:
    Areal += abs(((y[n]+y[n+1])*(x[n+1]-x[n]))/2)
    n +=1
print("Arealet av farten = ", round(Areal, 3))

plt.plot(x, y, "x")

# %%
