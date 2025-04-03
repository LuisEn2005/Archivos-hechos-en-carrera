# Dados dos números enteros, se desea determinar si el primero es divisible por el segundo, si es cierto desplegar
# “es divisible” y si no lo es, desplegar “no es divisible”.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

if numero1 % numero2 == 0:
    print(f"El numero {numero1} es divisible entre {numero2}.")
elif numero2 % numero1 == 0:
    print(f"El numero {numero2} es divisible entre {numero1}.")
else:
    print(f"Los numeros no son divisibles entre sí.")
    