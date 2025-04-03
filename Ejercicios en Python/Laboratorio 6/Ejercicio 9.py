# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden
# obtener en la evaluación comienzan en 0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0, 8, 12 o más, pero no valores intermedios
# entre las cifras mencionadas. A continuación, se muestra una tabla con los niveles correspondientes
# a cada puntuación. La cantidad de dinero conseguida en cada nivel es de S/ 2400.00 multiplicada por
# la puntuación del nivel.
#      Nivel       Puntuación
#   Inaceptable        0
#    Aceptable         8
#    Meritorio         12
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la
# cantidad de dinero que recibirá el usuario.

nombre = input("Ingrese su nombre: ")
puntos = int(input("Ingrese su puntuación (0,8,12 o más): "))

cantidad_dinero = 2400

if puntos == 0:
    print(f"El empleado {nombre} tiene una puntuacion de {puntos}") 
    print("Su nivel de rendimiento es Inaceptable")
    print("No recibirá paga.")
elif puntos == 8:
    paga = puntos * cantidad_dinero
    print(f"El empleado {nombre} tiene una puntuacion de {puntos}") 
    print("Su nivel de rendimiento es Aceptable")
    print(f"Recibirá una paga de S/{paga} soles")
elif puntos >= 12:
    paga = puntos * cantidad_dinero
    print(f"El empleado {nombre} tiene una puntuacion de {puntos}") 
    print("Su nivel de rendimiento es Meritorio")
    print(f"Recibirá una paga de S/{paga} soles")
else:
    print("Ese puntaje no esta disponible.")
    