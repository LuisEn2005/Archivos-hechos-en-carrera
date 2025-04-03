# Implementar funciones que permitan generar una lista, insertando los elementos en la parte inicial,
# media y final.

def inicial(numero):
    while numero != 0:
        lista.append(numero)
        numero = int(input("Introduzca un numero: "))
    return lista
def media(numero):
    while numero != 0:
        pos = int(len(lista))
        numero = int(input("Introduzca un numero: "))
        if numero != 0:
            lista.insert(pos,numero)
    return lista
def final(numero):
    while numero != 0:
        pos = int(len(lista))
        numero = int(input("Introduzca un numero: "))
        if numero != 0:
            lista.insert(pos,numero)
    return lista
lista = []
numero = int(input("Introduzca un numero: "))
Lista1 = inicial(numero)
Lista2 = media(numero)
Lista3 = final(numero)
print(Lista1)
print(Lista2)
print(Lista3)