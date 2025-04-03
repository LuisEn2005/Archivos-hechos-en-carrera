def media(lista,n):
    s=0
    for i in lista:
        s=s+i
    return s/n
lista = [1,2,3,4]
n = len(lista)
print(media(lista,n))
