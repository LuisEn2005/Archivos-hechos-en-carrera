# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores
# a S/ 1500 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
# por pantalla si el usuario tiene que tributar o no.

edad = int(input("Introduzca su edad: "))
ingresos = int(input("Introduzca sus ingresos: "))

if (edad > 18) and (ingresos >= 1500):
    print(f"Sus ingresos son {ingresos} y debe tributar")
else:
    print("Ud. no debe tributar")
