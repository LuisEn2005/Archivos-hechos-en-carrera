# Obtener la media aritmética de 3 valores ingresados por teclado y redondeado a 2 decimales.
a = float(input("Ingrese un 1er número: "))
b = float(input("Ingrese un 2do número: "))
c = float(input("Ingrese un 3er número: "))

d = (a + b + c)/2

print("{:.2f}".format(d))