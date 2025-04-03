# Utilice el bucle for anidado para imprimir números en patrones. Cada número se imprime un número de
# veces correspondiente a su propio número de forma ascendente.
# 1
# 2 2
# 3 3 3
# 4 4 4 4

numero = int(input("Introduzca el numero límite: "))

for fila in range(0,numero + 1):
    for columna in range(0,fila):
        print(f"{fila}", end=" ")
    print()