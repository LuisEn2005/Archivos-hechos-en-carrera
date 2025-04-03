def PrimeraMatriz(Matriz,filas,columnas):
    x = 1
    for i in range(filas):
        for j in range(columnas):
            Matriz[i][j] = x
            x = x + 1
            print(Matriz[i][j],end=" ")
        print()

def SegundaMatriz(Matriz,filas,columnas):
    for i in range(filas,0):
        for j in range(columnas):
            Matriz[i][j] = filas + columnas + 1
            print(Matriz[i][j],end=" ")
        print()
            
def TerceraMatriz(Matriz,filas,columnas,):
    for i in range(filas,0):
        for j in range(columnas):
            Matriz[i][j] = (i + 1) - j
            print(Matriz[i][j],end=" ")
        print()
        
Matriz = []
filas = int(input("Introduzca la cantidad de filas: "))
columnas = int(input("Introduzca la cantidad de columnas: "))
Matriz = [0] * filas
for i in range(filas):
    Matriz[i] = [0] * columnas
PrimeraMatriz(Matriz,filas,columnas)
SegundaMatriz(Matriz,filas,columnas)
TerceraMatriz(Matriz,filas,columnas)