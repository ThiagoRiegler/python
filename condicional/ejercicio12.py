sueldo = float(input("Ingrese el sueldo: "))

if sueldo < 1000:
    aumento = sueldo * 0.15
    sueldo = sueldo + aumento

print("El sueldo es:", sueldo)
