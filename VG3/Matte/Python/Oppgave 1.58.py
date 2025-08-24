#%%

n = 10 #Antall ledd i rekken

a1 = float(input("Hva er a1?"))
k = float(input("Hva er k?"))


def summerGeoRekke (a1, k):
    return (a1*(k**n-1)/(k-1))

print("Summen er :", round(summerGeoRekke(a1, k), 4))
# %%
