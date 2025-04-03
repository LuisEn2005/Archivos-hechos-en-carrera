numero = int(input("Introduzca un numero: "))
Lista = []
i = 0
mayor = 0
menor = 0

while numero != 0:
    Lista.append(numero)
    numero = int(input("Introduzca un numero: "))
    
    if Lista[i] > mayor:
        mayor = Lista[i]
    
    elif Lista[i] < menor:
        menor = Lista[i]
        
    i += 1
    
print(Lista)
print(f"El numero más alto de la lista es {mayor} y el numero más bajo de la lista es {menor}")