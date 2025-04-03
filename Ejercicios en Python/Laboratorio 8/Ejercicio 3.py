# Ejercicio 3
# Escriba un programa que imprima la forma de un diamante con (*) utilizando bucles anidados.
#      *
#     * *
#    * * *
#   * * * *
#    * * *
#     * *
#      *

numero = int(input("Introduzca el número límite: "))

for fila in range(numero):
    print(" "*(numero-fila), "*"*(fila*2+1))
for fila in range(numero-2, -1, -1):
    print(" "*(numero-fila), "*"*(fila*2+1))
    