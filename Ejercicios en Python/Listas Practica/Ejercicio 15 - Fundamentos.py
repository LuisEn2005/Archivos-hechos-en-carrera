# Mostrar el contenido de una lista de forma inversa.

def mostrarInversa(Lista):
    for elementos in range(len(Lista)):
        print(Lista[len(Lista)-1-elementos])

Lista = [1,2,3,4,5,6,7]

mostrarInversa(Lista)