cantidad = int(input("Cuantos numeros va a introducir? "))
Lista = []
negativos = 0
positivos = 0
for i in range(cantidad):
    numero = int(input("Introduzca un numero: "))
    Lista.append(numero)
    if Lista[i] > 0:
        positivos += 1
    if Lista[i] < 0:
        negativos += 1

print(f"La cantidad de numeros positivos es {positivos} y la cantidad de numeros negativos es {negativos}")