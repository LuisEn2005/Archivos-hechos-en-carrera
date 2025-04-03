cantidad = int(input("Cuantos notas va a ingresar? "))
Lista = []
mayor = 0
menor = 20


for i in range(cantidad):
    numero = int(input("Introduzca una nota: "))
    if numero <= 20 and numero >= 0:
        Lista.append(numero)
        if Lista[i] > mayor:
            mayor = Lista[i]
        if Lista[i] < menor:
            menor = Lista[i]

print(Lista)
print(f"El numero Mayor es {mayor} y el numero Menor es {menor}")
