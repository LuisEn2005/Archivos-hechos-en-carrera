# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está 
# formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
# el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
# pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo H o M: ")

abecedario_antes_de_M = ("A","B","C","D","E","F","G","H","I","J","K","L","M")
abecedario_despues_de_N = ("N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

if nombre.startswith(abecedario_antes_de_M) and sexo == "M":
    print("Pertenece al grupo A.")
elif nombre.startswith(abecedario_despues_de_N) and sexo == "H":
    print("Pertenece al grupo A.")
else:
    print("Pertenece al grupo B.")
