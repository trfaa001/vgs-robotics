#%%
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

data = np.array(loadtxt("co2.txt", delimiter="\t")) #Gjøre om text filen til en matrise vi kan bruke i koden

x_verdier = []
y_verdier = []

x = 1 #Setter den til 1 sånn at vi sammenligner med verdien etter

for i in data:
    nextVal = data[x][1] #Kalkulerer utslippet neste år
    differanse = nextVal - i[1] #sammenligner differansen mellom dette året og neste
    
    if x+1 < len(data): # vis x ikke har gått utenfor området til matrisen
        x+=1
    x_verdier.append(i[0])
    y_verdier.append(differanse)

plt.title("Økning av uslipp gjennom årene") #Tittel til grafen
plt.xlabel("år")    #Tittel til x-aksen
plt.ylabel("Økning av Co2 utslipp") #Tittel til y-aksen
plt.grid()  #Viser rutenett
plt.plot(x_verdier, y_verdier)
# %%
