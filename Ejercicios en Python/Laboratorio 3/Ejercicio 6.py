#Ingrese 1 número por teclado e implemente la siguiente ecuación de segundo grado: 2x^2–5x–3=0

print("Introduzca un numero para resolver la ecuación: 2x^2-5x-3=0")
x = int(input("Ingrese un número: "))

def Ecuacion(x):
    ecuacion = 2 * (x ** 2)- 5 * x - 3
    print(f"La respuesta de la ecuación es: {ecuacion}")
Ecuacion(x)