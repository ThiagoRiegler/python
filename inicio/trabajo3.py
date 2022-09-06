print("--------------------------")
print("Ejercicio 3: PUNTAJE FINAL")
print("--------------------------")

print("Ingrese numero de respuestas correctas: ")
rc = int(input())
print("Ingrese numero de respuestas incorrectas: ")
ri = int(input())
print("Ingrese numero de respuestas en blanco: ")
rb = int(input())

prc = rc*3
pri = ri*-1
prb = rb*0

pf = prb + pri + prc

print("Puntaje final:", pf)