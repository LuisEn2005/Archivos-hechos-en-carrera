"""3. Determinar cuántos números múltiplos de 3 y cuántos múltiplos de 7 hay en una lista.""" 

def multiplos(Lista):
    multiplode3 = 0
    multiplode7 = 0
    for numeros in range(len(Lista)):
        if Lista[numeros] % 3 == 0:
            multiplode3 += 1
        if Lista[numeros] % 7 == 0:
            multiplode7 += 1
    print(f"Hay {multiplode3} multiplos de 3 en la lista")
    print(f"Hay {multiplode7} multiplos de 7 en la lista")
    
Lista = [3,9,4,5,7,49,8,14]
multiplos(Lista)