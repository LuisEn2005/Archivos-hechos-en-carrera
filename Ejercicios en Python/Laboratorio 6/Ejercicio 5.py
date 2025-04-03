#Construya un algoritmo que solicite el ingreso de 2 de los 3 colores primarios e indique el color generado.

print("Estos son los 3 colores primarios (rojo,amarillo,azul)")
color1 = input("Introduzca un color primario:\n")
color2 = input("Introduzca otro color primario:\n")

if color1 == "rojo" and color2 == "amarillo" or color1 == "amarillo" and color2 == "rojo":
    print(f"La combinacion del color {color1} y la combinacion del color {color2} nos da: naranja")
elif color1 == "rojo" and color2 == "azul" or color1 == "azul" and color2 == "rojo":
    print(f"La combinacion del color {color1} y la combinacion del color {color2} nos da: morado")
elif color1 == "azul" and color2 == "amarillo" or color1 == "amarillo" and color2 == "azul":
    print(f"La combinacion del color {color1} y la combinacion del color {color2} nos da: verde")
else:
    print("El color que introdujo no es un color primario, asegúrese de escribir el color en minúsculas")