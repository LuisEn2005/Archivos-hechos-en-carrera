# Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en
# esa frase y la cantidad.

def obtener_vocales(frase):
    vocales = 'aeouiAEOUI'
    return([conteo for conteo in frase if conteo in vocales])

frase = input("Introduzca una frase: ")

print(f"las vocales que aparecen en la frase son {obtener_vocales(frase)} y hay {len(obtener_vocales(frase))} vocales")
