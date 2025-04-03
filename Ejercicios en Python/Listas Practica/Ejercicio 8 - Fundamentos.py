# Intercambiar la fila X con la fila Y
def ingresarValores(Matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            Matriz[i][j]= int(input(f"Introduzca el valor en la posicion {(i,j)}: "))

def mostrarMatriz(Matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print(Matriz[i][j],end=" ")
        print()
        
def intercambiarFila(Matriz,columnas,x,y):
    for i in range(columnas):
        aux = Matriz[x][i]
        Matriz[x][i] = Matriz[y][i]
        Matriz[y][i] = aux
        
Matriz = []
filas = int(input("Introduzca un numero de filas: "))
columnas = int(input("Introduzca un numero de columnas: "))
Matriz = [0]*filas
for i in range(columnas):
    Matriz[i]=[0]*columnas

ingresarValores(Matriz,filas,columnas)
mostrarMatriz(Matriz,filas,columnas)
x=int(input("Elija la fila a cambiar (1,2,3): "))
y=int(input(f"Elija la fila a cambiar con {x}: "))
intercambiarFila(Matriz,columnas,x-1,y-1)
mostrarMatriz(Matriz,filas,columnas)
    