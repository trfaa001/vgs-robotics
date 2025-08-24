#%%
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

data = np.array(loadtxt("co2.txt", delimiter="\t")) #Gjøre om text filen til en matrise vi kan bruke i koden

#lage lister for verdier på x- og y-aksen
x_verdier = []
y_verdier = []

for i in data:
    x_verdier.append(i[0])  #Legg til i liste for x-verdier
    y_verdier.append(i[1])  #Samme for y-verdier

plt.title("Utslipp gjennom årene")  # tittel på grafen
plt.xlabel("år")                       # x-akse-tittel
plt.ylabel("Co2")                     # y-akse-tittel
plt.grid()                                  # viser rutenett
plt.plot(x_verdier, y_verdier)
# %%
