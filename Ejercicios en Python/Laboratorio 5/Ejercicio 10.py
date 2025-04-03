# En una playa de estacionamiento del Sr. Pedro cobran S/. 2.5 por hora o fracción. Implemente un programa 
# que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, conociendo el tiempo de
# estacionamiento en horas y minutos.

import math as m

print("¿cuánto cobra el Sr. Pedro?")

horas=int(input("ingrese la cantidad de horas: "))
minutos=int(input("ingrese la cantidad de minutos: "))

var_a = minutos / 60
var_b = m.ceil(horas + var_a)
var_c = 2.5

if(horas > 0):
    precio = var_c * var_b
    print(f"El precio a pagar en soles es {precio}")