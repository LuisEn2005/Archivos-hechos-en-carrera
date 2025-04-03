# Elaborar un programa en python que permita calcular el número de micro
# discos 3 .5 necesarios para hacer una copia de seguridad, de la información
# almacenada en un disco cuya capacidad se conoce. Hay que considerar que el
# disco duro está lleno de información, además expresado en gigabyte. Un
# micro disco tiene 1.44 megabyte y un gigabyte es igual a 1,024 megabyte.
import math as m
capacidad = float(input("ingrese la capacidad de los discos en mb: "))
Disco_Duro = int(input("ingrese el tamaño de la información a respaldar en mb: "))
numdis = m.ceil(Disco_Duro/capacidad)
print("usted necesita", numdis, "discos para realizar la copia de seguridad")