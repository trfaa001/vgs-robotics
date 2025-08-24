#%%

Areal = 0

n = int(input("Hvor mange firkanter"))
a = float(input("Hvor skall integralet starte"))
b = float(input("Hvor skall integralet ende"))

delta_x = (b-a)/n

x_i = a

def f(x):
    #return 2*x+3
    #return (9-(x-4)**2)**(1/2)
    return x**2

for i in range(n):
    Areal += f(x_i)*delta_x
    x_i += delta_x
print("Venstre tilnærming", Areal)

print("")
Areal = 0
x_i = a

for i in range(n):
    Areal += f(x_i+delta_x)*delta_x
    x_i += delta_x
print("Høyre tilnærming", Areal)

print("")
Areal = 0
x_i = a

for i in range(n):
    Areal += f(x_i+(delta_x/2))*delta_x
    x_i += delta_x
print("Midtpunkt tilnærming", Areal)
# %%
