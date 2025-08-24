#%%
import matplotlib.pyplot as plt

#Konstante variabler
g = 9.81  #tyngdeakselerasjon
k = 0.32  #luftmotstandstall
dt = 0.001 #Tids mellomrom mellom kalkulasjoner

#Variabler
s = 0
v = 0
t = 0

#Opprette lister
s_verdier = []  #Posisjon
t_verdier = []  #Tid
v_verdier = []  #Hastighet

print("Fall med luftmotstand")

#Input fra bruker
m = float(input("Hva er massen til gjenstanden i kg?"))
s_slutt = float(input("Hvor langt faller gjenstanden (i meter)?"))

G = m*g #Tyngden til gjenstanden

#Funksjoner
def a(v):   #Akselerasjon som funksjon av fart
    L = k*v**2 #Luftmotstand
    sum_F = G-L #Summen av kreftene
    aks = sum_F/m #Akselerasjon
    return aks

while s < s_slutt:
    v = v+a(v)*dt #Beregne den nye farten
    s = s+v*dt  #Beregne strekningen den har fallt
    t = t+dt #Beregne tid passert
    
    #Legg inn nye verdier beregnet inn i lister
    s_verdier.append(s)
    t_verdier.append(t)
    v_verdier.append(v)

L = k*v**2 #Luftmotstanden på slutten

v = round(v, 1)
s = round(s, 1)
t = round(t, 1)
L = round(L, 1)
G = round(G, 1)

print("Tyngden til gjenstanden: ", G, "N")
print("Luftmotstand på slutten av fallet: ", L, "N")

print("")   #Spacer

print("Sluttid:", t, "s")    
print("Slutthastighet:", v, "m/s")  

plt.title("Strekning som funskjon av tid") #Tittel til grafen
plt.xlabel("$t$ (s)")   #Tittel til x-aksen
plt.ylabel("$s$ (m)") #Tittel til y-aksen
plt.grid()  #Viser rutenett
plt.plot(t_verdier, s_verdier)
plt.show()


print("Oppgave 26")

def v():
    print("lol")
    
# %%
