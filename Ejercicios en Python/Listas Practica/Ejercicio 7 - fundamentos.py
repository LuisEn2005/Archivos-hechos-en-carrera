# Sumar dos matrices de MxN.
def ingresarValoresM(MatrizM,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            MatrizM[i][j]= int(input(f"Introduzca el valor en la posicion {(i,j)}: "))
            
def ingresarValoresN(MatrizN,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            MatrizN[i][j]= int(input(f"Introduzca el valor en la posicion {(i,j)}: "))

def mostrarMatrizM(MatrizM,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print(MatrizM[i][j],end=" ")
        print()
        
def mostrarMatrizN(MatrizN,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print(MatrizN[i][j],end=" ")
        print()
        
def sumaMatrices(MatrizM,MatrizN,filas):
    for i in range(filas):
        for j in range(columnas):
            print(MatrizM[i][j] + MatrizN[i][j],end=" ")
        print()
    

filas = int(input("Introduzca un numero de filas: "))
columnas = int(input("Introduzca un numero de columnas: "))

MatrizM = []
MatrizN = []

MatrizM = [0]*filas
for i in range(columnas):
    MatrizM[i]=[0]*columnas
    
MatrizN = [0]*filas
for i in range(columnas):
    MatrizN[i]=[0]*columnas
    
ingresarValoresM(MatrizM,filas,columnas)
ingresarValoresN(MatrizN,filas,columnas)
mostrarMatrizM(MatrizM,filas,columnas)
mostrarMatrizN(MatrizN,filas,columnas)
sumaMatrices(MatrizM,MatrizN,filas)
