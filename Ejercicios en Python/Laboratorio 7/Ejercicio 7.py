# Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando
# todos los números enteros positivos que hay entre el 1 y ese número.
factorial = 1
numero = int(input("Introduzca un número: "))
for enteros_de_1_numero in range(1,numero + 1):
    factorial *= enteros_de_1_numero
print(f"El factorial de {numero} es {factorial}")
