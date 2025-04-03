# 1. Recorrer una lista que contiene las vocales y mostrarlas.

def recorrer(Lista):
    for i in range(len(Lista)):
        print(f"La vocal numero {i+1} es: {Lista[i]}")
        
Lista = ["a","e","i","o","u"]
recorrer(Lista)