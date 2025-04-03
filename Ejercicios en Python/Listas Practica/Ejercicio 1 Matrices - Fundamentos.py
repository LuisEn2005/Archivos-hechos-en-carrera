def ingresar(Matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            Matriz[i][j] = int(input("Valor? "))
            print(Matriz)
            
def mostrar(Matriz,fila,columna):
    for i in range(fila):
        for j in range(columna):
            print(Matriz[i][j],end=" ")
        print()
def suma(Matriz,fila,columna):
    s=0
    for i in range(fila):
        for j in range(columna):
            s=s+Matriz[i][j]
    return s
def sumaFila(Matriz,fila,columna):
    for i in range(fila):
        s=0
        for j in range(columna):
            s=s+Matriz[i][j]
        print("Suma de la fila",i+1,"=",s)
def sumaColumna(Matriz,fila,columna):
    for i in range(columna):
        s=0
        for j in range(fila):
            s=s+Matriz[j][i]
        print("Suma de la columna",i+1,"=",s)

Matriz=[]
fila=int(input("Cantidad de filas? "))
columna=int(input("Cantidad de columnas? "))
Matriz=[0]*fila
for i in range(fila):
    Matriz[i]=[0]*columna
    
ingresar(Matriz,fila,columna)
mostrar(Matriz,fila,columna)
sumaFila(Matriz,fila,columna)
sumaColumna(Matriz,fila,columna)
print(Matriz)