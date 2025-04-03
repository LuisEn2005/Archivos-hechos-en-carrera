""" 2. Ingresar N valores a una lista y mostrar el contenido. Realizar por medio de los tres
métodos revisados en clase.
"""
def mostrarContenido(cantidad,Lista):
    for elementos in range(cantidad):
        numero = int(input("Introduzca el numero que va a poner: "))
        Lista.append(numero)
    print(Lista)
cantidad = int(input("Ingrese la cantidad de valores: "))    
Lista = []

mostrarContenido(cantidad,Lista)