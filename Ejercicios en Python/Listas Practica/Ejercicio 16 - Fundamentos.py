# Copiar el contenido en forma inversa en otra lista.

def insertarLista(Lista,cantidad):
    for elementos in range(cantidad):
        numero = int(input("Introduzca un numero para la lista: "))
        Lista.append(numero)
        
def mostrarLista(Lista):
    print(Lista)
    
def invertirLista(Lista,listaInvertida):
    for elementos in range(len(Lista)):
        numero = Lista[len(Lista)-1-elementos]
        listaInvertida.append(numero)
    print(listaInvertida)
    
cantidad = int(input("Introduzca la cantidad de elementos para la lista: "))
Lista = []
listaInvertida = []

insertarLista(Lista, cantidad)
mostrarLista(Lista)
invertirLista(Lista, listaInvertida)