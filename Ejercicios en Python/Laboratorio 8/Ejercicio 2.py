# Utilice el bucle for anidado para imprimir números en patrones. Cada número se imprime un número de
# veces correspondiente a su propio número de forma descendente.
# 4 4 4 4
# 3 3 3
# 2 2
# 1

numero = int(input("Introduzca el numero límite: "))

for columna in range(numero,-1,-1):
    for fila in range(0,columna):
        print(f"{columna}", end=" ")
    print()