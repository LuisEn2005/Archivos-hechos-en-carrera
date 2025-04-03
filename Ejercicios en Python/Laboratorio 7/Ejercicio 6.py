# Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.

sumatoria = 0
for numeros in range(0,101):
    if numeros % 3 == 0:
        sumatoria += numeros
print(f"la sumatoria de todos los numeros multiplos de 3 entre el 0 y el 100 es {sumatoria}")
