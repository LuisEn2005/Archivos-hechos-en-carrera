# Ingresar N números enteros a una lista y hallar el promedio

def ingresarNumeros(Lista, cantidad):
    for ubicacion in range(cantidad):
        numero = int(input("Introduzca el numero: "))
        Lista.append(numero)
        
def sacarPromedio(Lista):
    suma = 0        
    for ubicacion in range(len(Lista)):
        suma += Lista[ubicacion]
        
    promedio = suma / len(Lista)
    
    print(f"El promedio de los numeros en la lista es: {promedio}")
    
Lista = []
cantidad = int(input("Introduzca la cantidad de numeros: "))

ingresarNumeros(Lista, cantidad)
sacarPromedio(Lista)