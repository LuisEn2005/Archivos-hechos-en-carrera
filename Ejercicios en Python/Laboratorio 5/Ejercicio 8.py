# Implemente un programa, que, dada la cantidad de artículos para su compra, debe escribir “Ve a Caja Rápida” 
# solo en caso de que la cantidad de artículos sea menor igual que 10.

cantidad_de_articulos = int(input("Introduzca la cantidad de articulos que va a llevar: "))

if cantidad_de_articulos <= 10:
    print("Pase a Caja Rápida.")
else:
    print("Ud. no puede pasar por Caja Rápida.")