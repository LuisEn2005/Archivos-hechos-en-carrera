# Un alumno de Ciencias de la Computación desea saber cuál será su
# calificación final en el curso de algoritmos. Dicha calificación se compone de
# los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
# Ingrese todos los datos por teclado y muestre el promedio final del alumno.
Calif_parcial1 = int(input("Ingrese la calificacion de su primer parcial: "))
Calif_parcial2 = int(input("Ingrese su calificación de su segundo parcial: "))
Calif_parcial3 = int(input("Ingrese su calificación de su tercer parcial: "))
Calif_examen_final = int(input("Ingrese su calificación del examen final: "))
Calif_trabajo_final = int(input("Ingrese su calificación del trabajo final: "))

promedio1 = (Calif_parcial1 + Calif_parcial2 + Calif_parcial3)/3

promedio_total = promedio1 * 0.55 + Calif_examen_final * 0.30 + Calif_trabajo_final * 0.15 

print(f"La calificación total del alumno es de: {promedio_total}")