# Implemente un programa en donde 2 jugadores tiran los dados y el ganador debe ser el que tenga el número 
# mas alto. Toda la información debe mostrar por pantalla.
import random

jugador_1 = random.randint(1,6)
jugador_2 = random.randint(1,6)

print(f"el jugador 1 sacó: {jugador_1}")
print(f"el jugador 2 sacó: {jugador_2}")

if jugador_1 > jugador_2:
    print("El jugador 1 gana.")
elif jugador_2 > jugador_1:
    print("El jugador 2 gana.")
else:
    print("Salieron numeros iguales.")
    

