# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al
# usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede
# entrar gratis, si tiene entre 4 y 18 años debe pagar S/ 5.00 y si es mayor de 18 años, S/ 10.00

edad = int(input("Introduzca su edad: "))

if edad > 0 and edad <= 4: 
    print("Ud. entra gratis")
elif edad > 4 and edad <= 18:
    print("Ud. debe pagar S/ 5.00 soles.")
elif edad > 18:
    print("Ud. debe pagar S/10.00 soles.")
else:
    print("Esa edad no existe.")