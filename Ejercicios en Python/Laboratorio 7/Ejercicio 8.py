# Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con
# los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la 
# secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
numero1 = 0
numero2 = 1
print(numero1)
print(numero2)
for fibonacci in range(0,8):
    numero3 = numero1 + numero2
    print(numero3)
    numero1 = numero2
    numero2 = numero3
