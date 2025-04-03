numeros = int(input("Cuantos numeros desea ingresar? "))
Lista = []
suma = 0
for i in range(numeros):
    num = int(input("Numero? "))
    Lista.append(num)
    suma += Lista[i]
    
promedio = suma/len(Lista)

print(f"El promedio de los numeros en la lista es {promedio}")