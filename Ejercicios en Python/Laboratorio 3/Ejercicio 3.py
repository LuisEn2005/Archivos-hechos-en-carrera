# Dado 2 números ingresados por teclado, realice las 4 operaciones básicas.
a = int(input("Ingrese un 1er número: "))
b = int(input("Ingrese un 2do número: "))

def operaciones(a,b):
    multiplicacion = a * b
    division = a / b
    suma = a + b
    resta = a - b ;
    print(f"la multiplicacion entre a y b es: {multiplicacion}")
    print(f"la division entre a y b es: {float(division)}")
    print(f"la suma entre a y b es: {suma}")
    print(f"la resta entre a y b es: {resta}")
operaciones(a,b)