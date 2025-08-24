a = int(input("Hvor mange partall skal summeres?"))
sum = 0

for partall in range(2, 2*a + 1, 2):
    print(partall)
    sum += partall

print("Summen av de", a, "første partallene er:", sum)