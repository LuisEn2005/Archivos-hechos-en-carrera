# Calcule el área de un triángulo, utilizando la librería math, los 3 valores de los lados deben ser ingresados por teclado.
import math as m
Lado1 = int(input("Ingrese la medida del primer lado: "))
Lado2 = int(input("Ingrese la medida del secundo lado: "))
Lado3 = int(input("Ingrese la medida del tercer lado: "))

semiperimetro = (Lado1 + Lado2 + Lado3) / 2

formula = semiperimetro * (semiperimetro - Lado1) * (semiperimetro - Lado2) * (semiperimetro - Lado3)

area_T = m.sqrt(formula)

print(f"El area del Triángulo es: {area_T}")