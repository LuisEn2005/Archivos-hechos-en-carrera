#Ingrese 3 números por teclado e implemente la siguiente ecuación de tercer grado: x^3–4y^2–5z–10=0

x = int(input("Ingrese un 1er número: "))
y = int(input("Ingrese un 2do número: "))
z = int(input("Ingrese un 3er número: "))

ecuacion = x ** 3 - 4 * (y ** 2) - 5 * z - 10

print(f"La respuesta de la ecuación es: {ecuacion}")