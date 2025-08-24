#%%
i = 1
Ferdig = False
sigma = 0

while Ferdig == False: #Til b er funnet
    i += 1
    
    LeggTil = i**2+3*i   #Formel vi får oppgitt
    sigma += LeggTil #Legg den nye tallet inn i summen

    print("Sigma ", i, ":", sigma)

    if sigma > 5800: # Stopp hvis vi kommer over målet
        Ferdig = True
    

print("Sluttsvar: ", i, "Eller", i-1)


# %%
