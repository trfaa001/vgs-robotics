
#tx er så lav som mulig
tx = 0.00000000000001
y = float(input("y = "))


def f(x):
    f = 2*x**2 - 7*x
    return f

#dette er f'(x)
print("Stigningstallet er: ", (f(y + tx) - f(y))/tx)
