# El siguiente código como lo harías con condicionales multiples:

#entrada = int(input('Introduce un número del 1 al 4:\n'))
# if entrada == 1:
#   print('Has seleccionado la opción número 1.')
# if entrada == 2:
#   print('Has seleccionado la opción número 2.')
# if entrada == 3:
#   print('Has seleccionado la opción número 3.')
# if entrada == 4:
#   print('Has seleccionado la opción número 4.')

entrada = int(input('Introduce un número del 1 al 4:\n'))
if entrada == 1:
    print("Has seleccionado la opción 1.")
elif entrada == 2:
    print("Has seleccionado la opción 2.")
elif entrada == 3:
    print("Has seleccionado la opción 3.")
elif entrada == 4:
    print("Has seleccionado la opcion 4.")
else:
    print("El numero ingresado no está en las opciones")