c = 0
x = 1

print("Ingrese 10 numeros: ")
for x in range(10):
    num = int(input())
    if num%2 == 0:
        c = c+1
    
print("Hay", c,"numeros pares")