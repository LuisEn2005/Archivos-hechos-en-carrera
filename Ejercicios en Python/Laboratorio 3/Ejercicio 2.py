# Dado 3 números ingresados por teclado, obtenga el promedio de los tres números.
a = int(input("Ingrese un 1er número: "))
b = int(input("Ingrese un 2do número: "))
c = int(input("Ingrese un 3er número: "))

d = (a + b + c) / 3

print("{:.0f}".format(d))
