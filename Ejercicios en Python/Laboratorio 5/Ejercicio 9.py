# En la escuela de artes de la universidad se tiene un costo de inscripción único de S/ 100 soles.
# Pero a los alumnos con promedio mayor o igual a 15 se les da un descuento del 30%.

costo = 100
costo_total = 100
promedio = int(input("Introduzca su promedio: "))
if promedio >= 15:
    costo_total = costo - costo * 0.3
    print(f"El costo total que debe pagar es {costo_total}")
else:
    print(f"El costo total que debe pagar es {costo_total}")
    