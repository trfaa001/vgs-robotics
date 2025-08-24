from pylab import *

print("Fall med luftmotstand")
print(" ")  # tom linje

# konstanter
g = 9.81  # tyngdeakselerasjon, m/s^2
k = 0.32  # luftmotstandstall, kg/m

# input
m = float(input("Hva er massen til gjenstanden i kg?"))
G = m*g          # tyngden til gjenstanden (N)
print(" ")       # tom linje

def a(v):        # akselerasjon (funksjon av fart)
  L = k*v**2     # luftmotstand (N)
  sum_F = G - L  # kraftsum (N)
  aks = sum_F/m  # akselerasjon (m/s^2)
  return aks
  
# startverdier
s = 0     # startposisjon, m
v = 0     # startfart, m/s
t = 0     # starttid, s
dt = 0.01 # lengde på tidssteg, s

# lagring av verdier i lister
s_verdier = [s]  # posisjon
v_verdier = [v]  # hastighet
t_verdier = [t]  # tid

# input 
s_slutt = float(input("Hvor langt faller gjenstanden (i meter)?"))
print(" ") #tom linje

# beregner hastighet, posisjon og tid
while s < s_slutt:  # betingelse
  v = v + a(v)*dt   # ny hastighet
  s = s + v*dt      # ny posisjon
  t = t + dt        # ny tid
  
  t_verdier.append(t)  # legger ny t-verdi i t-listen
  v_verdier.append(v)  # legger ny v-verdi i v-listen
  s_verdier.append(s)  # legger ny s-verdi i s-listen

# lager graf
plot(t_verdier, s_verdier)              
title("Strekning som funksjon av tid")  
xlabel("$t$ / s")                       
ylabel("$s$ / m")                       
grid()                                  
show()

L = k*v**2                    # luftmotstand på slutten 
L_svar = "{:.1f}".format(L)   # runder av til ett desimal

G_svar = "{:.1f}".format(G)   # runder av tyngden til ett desimal

t_svar = "{:.1f}".format(t)   # runder av til ett desimal
v_svar = "{:.1f}".format(v)   # runder av til ett desimal

print("Tyngden til gjenstanden:", G_svar, "N")
print("Luftmotstand på slutten av fallet:", L_svar, "N")
print(" ")  # tom linje 

print("Sluttid:", t_svar, "s")    
print("Slutthastighet:", v_svar, "m/s")
print(" ")    # tom linje
