# La liga de baloncesto de Arequipa esta seleccionando al equipo que los
# representara, por cada uno se lee el nombre y estatura. Implemente un
# programa que determine si la persona no tiene una estatura mayor a 1.70 mts
# inclusive.

nombre = input("Introduzca su nombre: ")
estatura = float(input("Introduzca su estatura en metros: "))

if estatura < 1.70:
    print("Su estatura es menor de 1.70 metros.")
else:
    print("Su estatura es mayor o igual de 1.70 metros")
