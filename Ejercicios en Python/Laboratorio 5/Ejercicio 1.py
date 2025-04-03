# Implemente un programa que lea un número por teclado y determine si su cubo es positivo o negativo.

numero = int(input("Introduzca un número: "))
if numero > 0:
    print(f"El numero {numero} es positivo.")
elif numero < 0:
    print(f"El numero {numero} es negativo.")
else:
    print("El numero es 0")
