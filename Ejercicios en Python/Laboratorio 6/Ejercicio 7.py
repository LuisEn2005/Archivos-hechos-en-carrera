# Dulcina es fábrica de golosinas del Perú dedicada a la comercialización de dulces a nivel nacional. Después 
# de una minuciosa evaluación, la empresa ha decidido asignarle la tarea de desarrollar un programa que 
# permita gestionar las ventas de dulces. Se le pide ingresar la siguiente información: cantidad de dulces a
# comprar, el tipo de dulce (1, 2 o 3) y muestre como salida, el tipo de dulce, el precio unitario, la 
# cantidad y el monto de la venta, teniendo en cuenta la siguiente política de descuento:
#Tipo de dulce Precio unitario   Cantidad    Descuento
#      1          S/ 4.00       Hasta 5       S/ 0.5
#                               Más de 5        5%
#      2          S/ 5.00       Hasta 6    Sin descuento
#                               Más de 6        3%
#      3          S/ 6.00       Más de 4        10%
# Implemente un programa que indique el monto a pagar.

cantidad_dulces = int(input("Introduzca la cantidad de dulces a comprar: "))
tipo_de_dulce = input("Introduzca el tipo de dulce que va a adquirir (1,2,3): ")

print(f"Ud. quiere {cantidad_dulces} dulces")

if tipo_de_dulce == "1":
    print("Ud. escogio el dulce de tipo 1")
    print("Con un precio unitario de 4")
    
    precio_unitario = 4
    
    if cantidad_dulces <= 5:
        monto_pagar = precio_unitario * cantidad_dulces * 0.5
        print(f"Ud. debe pagar {monto_pagar} soles")    
    else:
        monto_pagar = precio_unitario * cantidad_dulces * 0.05
        print(f"Ud. debe pagar {monto_pagar} soles")    
        
elif tipo_de_dulce == "2":
    print("Ud. escogió el dulce de tipo 2")
    print("Con un precio unitario de 5")
    
    precio_unitario = 5
    
    if cantidad_dulces <= 6:
        monto_pagar = precio_unitario * cantidad_dulces
        print(f"Ud. debe pagar {monto_pagar} soles")    
    else:
        monto_pagar = precio_unitario * cantidad_dulces * 0.03
        print(f"Ud. debe pagar {monto_pagar} soles")
        
elif tipo_de_dulce == "3":
    print("Ud. escogió el dulce de tipo 3")
    print("Con un precio unitario de 6")
    
    precio_unitario = 6
    
    if cantidad_dulces > 4:
        monto_pagar = precio_unitario * cantidad_dulces * 0.1
        print(f"Ud. debe pagar {monto_pagar} soles")
else:
    print("No existe ese tipo de dulce.")