#%%
import matplotlib.pyplot as plt

#Konstante variabler
g = 9.81  #tyngdeakselerasjon (m/s**2)
k = 0.32  #luftmotstandstall (kg/m)
dt = 0.001 #Tids mellomrom mellom kalkulasjoner (s)
dtu = 0.5 #Tids mellemrom for mer krevende kalkulasjoner (s)



print("Fall med luftmotstand")

#Input fra bruker
m = float(input("Hva er massen til gjenstanden i kg?"))
s_slutt = float(input("Hvor langt faller gjenstanden (i meter)?"))



#Funksjoner
def a(v,m):   #Akselerasjon som funksjon av fart
    L = k*v**2 #Luftmotstand
    G = m*g
    sum_F = G-L #Summen av kreftene
    aks = sum_F/m #Akselerasjon
    return aks

#Funksjon som simulerer fallet til et objekt
def sim(m,s_slutt):
    #Variabler
    s = 0   #Strekning (m)
    v = 0   #Fart (m/s)
    t = 0   #Tid (s)

    #Opprette lister
    s_verdier = []  #Posisjon
    t_verdier = []  #Tid
    v_verdier = []  #Hastighet
    
    while s < s_slutt:
        v = v+a(v, m)*dt #Beregne den nye farten
        s = s+v*dt  #Beregne strekningen den har fallt
        t = t+dt #Beregne tid passert
        
        #Legg inn nye verdier beregnet inn i lister
        s_verdier.append(s)
        t_verdier.append(t)
        v_verdier.append(v)
    
    L = k*v**2 #Luftmotstanden på slutten
    return L,s,t,v,G, t_verdier, s_verdier, v_verdier

L,s,t,v,G, t_verdier, s_verdier, v_verdier = sim(m,s_slutt)    

v = round(v,1)
s = round(s,1)
t = round(t,1)
L = round(L,1)
G = round(G,1)

print("Tyngden til gjenstanden: ", G, "N")
print("Luftmotstand på slutten av fallet: ", L, "N")

print("")   #Spacer

print("Sluttid:", t, "s")    
print("Slutthastighet:", v, "m/s")  

plt.title("Strekning som funskjon av tid") #Tittel til grafen
plt.xlabel("$t$ (s)")   #Tittel til x-aksen
plt.ylabel("$s$ (m)") #Tittel til y-aksen
plt.grid()  #Viser rutenett
plt.plot(t_verdier,s_verdier)
plt.show()


print("Oppgave 26")
print("a.")
m = 85 #Vi får vite at fallskjermhopperen er 85kg
s_slutt = 50 #Vi får vite at fallskjermhopperen faller 50m

L,s,t,v,G, t_verdier, s_verdier, v_verdier = sim(m,s_slutt) 

t = round(t, 1)

print("Fallskjermhopperen bruker nå ", t, "s, som tyder på at den økte vekten fikk hopperen til å akselerere raskere.")

print("b.")

m = 1

while v <= 30:
    L,s,t,v,G, t_verdier, s_verdier, v_verdier = sim(m,s_slutt) 
    m+=dtu
    #print("Vekten nå:", m)
    #print("Farten nå:", v)
    #print("Akselerasjonen er: ", a(v, m))
print("Hopperen må veie ",m, "kg for å nå terminalfarten på 30m/s på et fall på 50m.")   

print("")

print("Oppgave 27")

k = 0.1 #Endrer luftmotstandtallet
m = 10
s_slutt = 100

L,s,t,v,G, t_verdier, s_verdier, v_verdier = sim(m,s_slutt)  #Setter inn verdier som er gitt i oppgaven (10kg, 100m)

t = round(t, 1)

print("Det tokk", t, "s for at legemet på 10kg skulle falle ned 100kg med luftmostandtall på 0,1kg/m")
# %%