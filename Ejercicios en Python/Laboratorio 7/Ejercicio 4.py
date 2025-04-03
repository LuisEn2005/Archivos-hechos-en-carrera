# Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre
# el ingresado por el usuario y uno menos del doble del mismo.

numero_positivo = int(input("Introduzca un numero entero positivo: "))

numero_doble = numero_positivo * 2

for numero in range(numero_positivo,numero_doble):
    print(numero)
