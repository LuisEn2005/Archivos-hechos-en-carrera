# Implemente un programa que lea un número y escriba si es mayor que 100 y menor que 200.

numero = int(input("Introduzca un numero: "))

if (numero > 100) and (numero < 200):
    print(f"El numero {numero} es mayor de 100 y menor que 200.")
else:
    print(f"El numero {numero} no es mayor de 100 ni menor que 200.")