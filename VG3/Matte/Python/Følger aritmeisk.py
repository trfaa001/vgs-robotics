#%%

def aritmetisk(a1,d,m):
    nesteTall = a1
    for i in range(m):
        nesteTall += d
        print(nesteTall)
    return "ferdig"

a1 = int(input("Hva er det første tallet?"))
d = int(input("Hva er differansen?"))
m = int(input("Hvor mange tall vil du ha?"))

print("Første tall = ", a1)
print("Differansen er = ", d)
print("Antall ledd er = ", m)

print(aritmetisk(a1, d, m))
# %%
