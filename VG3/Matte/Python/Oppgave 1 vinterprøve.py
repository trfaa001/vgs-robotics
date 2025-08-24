
#Startverdier
n = 1
Summen = 0
intervall = 1

#Funksjonen nevt i oppgaven
def f(x):
    return 1/(x**2)

#Beregner ut summen ved å regne ut hvert tall og summere de sammen
for i in range(10**5): #Repeteres så mange ganger vi vil, et høyere tall vil oppnå en mer nøyaktig verdi for pi
    Summen += f(n)
    n += intervall

pi = (Summen*6)**0.5 #Fordi summen ikke resulterer i pi, men i pi^2/6 må vi snu om

print("Verdi for pi: ", pi)