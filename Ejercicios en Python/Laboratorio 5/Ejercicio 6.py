# Implemente un programa, tal que si la calificación de un alumno en un examen, es mayor de 10.5 
# escriba "aprobado" de lo contrario “desaprobado”.

calificacion = float(input("Introduzca la calificacion de su examen: "))

if calificacion >= 10.5:
    print(f"Usted está aprobado con una calificacion de {calificacion}")
else:
    print(f"Usted está desaprobado con una calificacion de {calificacion}")
