#%%

delta = 1E-4
Bevegd = 0

Sum = 0

startVerdi = 0
SluttVerdi = 5
n = 50

def f(x):
    return 2*x+1

while Bevegd < n:
    Sum += f(startVerdi)*delta
    Bevegd += delta


print("Summen", Sum)
# %%
