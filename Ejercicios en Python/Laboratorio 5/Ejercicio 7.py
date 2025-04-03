# Crear un programa que lea un número por teclado, y debe calcular su cuadrado si él número ingresado es par.
import math as m 

numero = int(input("Introduzca un numero: "))
if numero % 2 == 0:
    if numero != 0:
        z = m.pow(numero,2)
        print(f"el numero ingresado es par, elevado al cuadrado es {z}")
    elif numero == 0:
        print("El numero es 0")
else:
    print("El numero ingresado no es par")