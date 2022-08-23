x = int(input("Ingrese el valor de x: "))

e = 1
num = 1
den = 1
i = 1

while num/den > 0.000001:

    num = x * num
    den = den * i
    i = i + 1
    e = e + num / den

print("e elevado a", x, "es", e)