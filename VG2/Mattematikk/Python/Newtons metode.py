import math
import time


delta_x = 1E-8

e = 2.718281 # definerer konstanten e

xt = [3.9] #Lister over x verdier programmet har besøkt

antall_Prøvd = 0

max_nøyaktighet = False #Programmet har ikke truffet maximal nøyaktighet enda

def f(x):           #Funksjonen som vi finner nullpunkt til
    return e**x - x**2

def derivert_f(x):  #Numerisk derivasjon
    return (f(x+delta_x)-f(x))/(delta_x)

while max_nøyaktighet == False:
    xt.append(xt[-1] - (f(xt[-1]))/(derivert_f(xt[-1]))) #Bruker Newtons 
    
    antall_Prøvd+=1
    
    print("Fant bedre, dette er utregning: ", antall_Prøvd)
    print(xt[-1],",",f(xt[-1])) #Nyeste punkt som nærmer seg nullpunktet
    print(" ")
    
    if xt[-1] == xt[-2]: #Sjekker om programmet finner en ny verdi
        max_nøyaktighet = True
        
        print(" ")
        print("Programmet kan ikke finne noe nærmere nullpunktet!")
    
    time.sleep(1)
    