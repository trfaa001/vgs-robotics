#%%
# Programmet beregner bevegelsen til en 100-meter-løper
# som akselererer ut fra en startblokk. Bevegelsen
# presenteres som en v-s-graf.

import numpy as np
import matplotlib.pyplot as plt

# Informasjon om bevegelsen
s = 0  # startposisjon, m
v = 0  # startfart, m/s
t = 0  # starttid, s

# Simuleringsteknisk
s_slutt = 100    # sluttposisjon, m
dt = 0.01        # lengde på tidssteg, s
s_verdier = []  # liste med verdier for posisjon
v_verdier = []  # liste med verdier for fart

def a(v): # akselerasjonen er en funksjon av farten
  aks = -0.5*v + 6  # beregner akselerasjonen
  return aks        # returnerer akselerasjonen

# Løkka regner ut ny akselerasjon, fart og posisjon
# til løperen for hvert tidssteg
while s < s_slutt:     # etter 100 m er løpet over
  v = v + a(v)*dt      # beregner ny fart
  s = s + v*dt         # beregner ny posisjon
  t = t + dt           # øker tiden med dt
  s_verdier.append(s)  # legger s inn i posisjonslisten
  v_verdier.append(v)  # legger v inn i fartslisten

# Tegning av graf
plt.plot(s_verdier, v_verdier)              # lager grafen
plt.title("Fart som funksjon av posisjon")  # tittel på grafen
plt.xlabel("$s$ (m)")                       # x-akse-tittel
plt.ylabel("$v$ (m/s)")                     # y-akse-tittel
plt.grid()                                  # viser rutenett
plt.show()                                  # viser grafen
# %%
