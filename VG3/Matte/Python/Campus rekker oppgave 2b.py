#%%

summer = 0 #Den totale summen
interval = 1 #velg at i starter på 1

for i in range(100): #Prosessen skal skje 100 ganger
    sigma = interval/(interval+1) #Formel vi blir oppgitt
    summer += sigma #Legg den nye tallet inn i summen
    interval += 1 #Gå til neste tall
    

print("Sluttsvar: ", summer)


# %%
