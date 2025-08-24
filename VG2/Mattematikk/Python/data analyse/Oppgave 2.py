#%%
from pylab import loadtxt
import numpy as np
data = np.array(loadtxt("co2.txt", delimiter="\t")) #Gjøre om text filen til en matrise vi kan bruke i kode

# Sette/lage verdier
difference = 0
x = 1 #Setter den til 1 sånn at vi sammenligner med verdien etter

for i in data:
    nextVal = data[x][1] #Kalkulerer utslippet neste år
    new_difference = i[1] - nextVal #Kalkulerer nedgangen dette året
    if x+1 < len(data): # vis x ikke har gått utenfor området til matrisen
        x+=1    #setter x et år fram
    if difference < new_difference: #Sammenligner om nedgangen nå er høyere enn den høyeste funnet
        difference = new_difference #Lagre den høyeste oppgangen
        where = int(i[0]) ##Lagre hvor vi fant den høyeste nedgangen
print("Den største nedgangen skjedde fra år ",where," til det neste, og da var den en nedgang på ", difference)
# %%
