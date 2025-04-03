def insertar(Matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            Matriz[i][j]=int(input(f"Introduzca un numero para la posicion [{i}][{j}]: "))

def mostrarMatriz(Matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print(Matriz[i][j],end=" ")
        print()
        
def MayorNumDiagonalPrim(Matriz,filas,columnas):
    mayor = 0
    for i in range(filas):
        for j in range(columnas):
            if i == j and Matriz[i][j] > mayor:
                mayor = Matriz[i][j]
    print(f"El mayor numero en la Diagonal Primaria es: {mayor}")
    
def MayorNumDiagonalSec(Matriz,filas,columnas):
    j = columnas - 1
    mayor = 0
    for i in range(filas):
        #print(Matriz[i][j],end=" ")
        if Matriz[i][j] > mayor:
            mayor = Matriz[i][j]
        j=j-1
    print(f"El mayor numero en la Diagonal Secundaria es: {mayor}")
        
        
Matriz = []
filas = int(input("Introduzca la cantidad de filas: "))
columnas = int(input("Introduzca la cantidad de columnas: "))
Matriz = [0] * filas
for i in range(filas):
    Matriz[i] = [0] * columnas
insertar(Matriz,filas,columnas)
mostrarMatriz(Matriz,filas,columnas)
MayorNumDiagonalPrim(Matriz,filas,columnas)
MayorNumDiagonalSec(Matriz,filas,columnas)