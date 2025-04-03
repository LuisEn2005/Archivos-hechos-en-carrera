# Implemente un programa en donde 2 jugadores tiran los dados y el ganador
# debe ser el que tenga el número mas alto. Toda la información debe mostrar
# por pantalla.
import random
jugador1 = random.randrange(1,7)
jugador2 = random.randrange(1,7)
print(f"El jugador 1 obtuvo: {jugador1}")
print(f"El jugador 2 obtuvo: {jugador2}")
if jugador1 > jugador2:
    print("El jugador 1 gana")
elif jugador2 > jugador1:
    print("El jugador 2 gana")
else:
    print("Tocaron numeros iguales")