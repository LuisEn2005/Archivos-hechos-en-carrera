#Realiza un programa que reciba una cantidad de minutos y muestre por
#pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos
#son 16 horas y 40 minutos.

print("Ingrese la cantidad de minutos para convertir en horas.")
minutos = int(input("Ingrese la cantidad de minutos: "))

horas = minutos // 60 
minutos_residuo = minutos % 60
print(f"{minutos} minutos son {horas} horas y {minutos_residuo} minutos en total")