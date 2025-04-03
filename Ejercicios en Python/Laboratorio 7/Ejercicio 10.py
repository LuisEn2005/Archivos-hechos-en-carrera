# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese 
# rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible
# por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

año1 = int(input("Introduzca un año: "))
año2 = int(input("Introduzca otro año: "))


for bisiesto in range(año1,año2):
    if bisiesto % 4 == 0 and bisiesto % 10 == 0:
        print(bisiesto)