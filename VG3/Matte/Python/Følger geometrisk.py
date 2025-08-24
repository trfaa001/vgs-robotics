#%%

def aritmetisk(a1,r,m):
    nesteTall = a1
    for i in range(m):
        nesteTall *= r
        print(nesteTall)
    return "ferdig"

a1 = int(input("Hva er det første tallet?"))
r = int(input("Hva er forholdet?"))
m = int(input("Hvor mange tall vil du ha?"))

print("Første tall = ", a1)
print("Forholdet er = ", r)
print("Antall ledd er = ", m)

print(aritmetisk(a1, r, m))
# %%
