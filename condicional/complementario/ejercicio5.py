dist = float(input("Ingrese la distancia entre los vehiculos: "))
vel1 = float(input("Ingrese la velocidad del vehiculo 1: "))
vel2 = float(input("Ingrese la velocidad del vehiculo 2: "))

if vel1 > 0 and vel2 > 0:
    t = dist/(vel1 + vel2)
    print("El tiempo de encuentro es:", t, "segundos")
else:
    print("Error")
