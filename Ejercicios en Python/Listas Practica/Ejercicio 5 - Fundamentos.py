"""
Ingresar varios valores a una lista terminados en -1 (valor centinela). determinar cuántos de los
valores ingresados a la lista son números primos 
"""

def ingresarNumeros(Lista, numero):
    while numero != -1:
        Lista.append(numero)
        numero = int(input("Introduzca un numero: "))

def numerosPrimos(Lista):
    for recorrido in range(2,len(Lista) // 2 + 1):
        primos = True
        for ubicacion in range(2,recorrido):
            if ubicacion == recorrido:
                break
            if ubicacion % recorrido == 0:
                print(f"No es primo {ubicacion} es divisor")
                primos = False
            if primos == True:
                print(f"Es primo {ubicacion} no tiene divisor")
        
numero = int(input("Introduzca un numero: "))
Lista = []

ingresarNumeros(Lista, numero)
numerosPrimos(Lista)