#%%

n = 10 #Antall ledd i rekken
TotalSum = 0 #Lage variable for den totale summen

a1 = float(input("Hva er a1?"))
k = float(input("Hva er k?"))

a_n = a1

for i in range(n):
    TotalSum += a_n
    a_n *= k
print(TotalSum)

# %%
