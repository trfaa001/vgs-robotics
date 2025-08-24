#%%

from pylab import *
data = loadtxt("rakett.txt")
tid = data[:, 0]
fart = data[:, 1]
n = len(tid)

dt = tid[2]-tid[1]
s = 0

for i in range(n):
    s = s + abs(fart[i])*dt

print(round(s, 3))
# %%
