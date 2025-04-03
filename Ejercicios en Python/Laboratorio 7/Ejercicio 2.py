#Imprimir todos los números entre el 100 al 199 y al final muestre la sumatoria de todos los números.

sumatoria = 0

for numeros in range(100,200):
    print(numeros)
    sumatoria += numeros
print(f"La sumatoria de todos los numeros es {sumatoria}")
    