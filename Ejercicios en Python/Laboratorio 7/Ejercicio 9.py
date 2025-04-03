# Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o 
# negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
# No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje
# un error si no se ingresaron números positivos.

contador = 0
suma_positivos = 0
suma_negativos = 0
lista_de_positivos = []
lista_de_negativos = []

while contador < 6:
    numeros = int(input("Introduzca 6 numeros: "))
    contador += 1
    if numeros >= 0:
        lista_de_positivos.append(numeros)
        suma_positivos += numeros
    elif numeros < 0:
        lista_de_negativos.append(numeros)
        suma_negativos += numeros
if len(lista_de_positivos) == 0:
    promedio_positivos = None
else:
    promedio_positivos = suma_positivos / len(lista_de_positivos)
print(f"El promedio de los numeros positivos es: {promedio_positivos}")
print(f"La sumatoria de los numeros negativos es: {suma_negativos}")

