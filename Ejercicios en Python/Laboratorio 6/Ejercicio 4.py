# Los tramos impositivos para la declaración de la renta en Perú son los siguientes:

# Renta            Tipo impositivo
# Menos de 1 UIT          5%
# Entre 1 UIT y 5 UIT    10%
# Entre 5 UIT y 10 UIT   15%
# Más de 10 UIT          20%

# Escribir un programa que pregunte al usuario su renta anual y muestre por
# pantalla el tipo impositivo que le corresponde.

renta_anual = int(input("Introduzca su renta anual: "))
UIT = 4950
if renta_anual < UIT:
    renta_anual += renta_anual * 0.05
    print(f"Ud. debe pagar {renta_anual} soles en total.")
elif renta_anual > UIT and renta_anual < 5 * UIT:
    renta_anual += renta_anual * 0.1
    print(f"Ud. debe pagar {renta_anual} soles en total.")
elif renta_anual > 5 * UIT and renta_anual < 10 * UIT:
    renta_anual += renta_anual * 0.15
    print(f"Ud. debe pagar {renta_anual} soles en total.")
elif renta_anual > 10 * UIT:
    renta_anual += renta_anual * 0.2
    print(f"Ud. debe pagar {renta_anual} soles en total.")
    
