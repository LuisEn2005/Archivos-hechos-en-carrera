# La pizzería Presto ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# • Ingredientes vegetarianos: Pimiento y tofu.
# • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
# respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un
# ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar
# por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido al asistente Presto para pedir pizzas vegetarianas y no vegetarianas.")
tipo_de_pizza = input("Introduzca que tipo de pizza va a ordenar (vegetariana o no vegetariana):\n")
if tipo_de_pizza == "vegetariana":
    ingrediente_extra = input("Que ingrediente extra quiere añadir? (pimiento y tofu):\n")
    if ingrediente_extra == "pimiento":
        print(f"La pizza elegida es vegetariana además lleva {ingrediente_extra}, mozzarella y tomate.")
    elif ingrediente_extra == "tofu":
        print(f"La pizza elegida es vegetariana además lleva {ingrediente_extra}, mozzarella y tomate.")
    else:
        print("No se puede introducir ese ingrediente")
elif tipo_de_pizza == "no vegetariana":
    ingrediente_extra = input("Que ingrediente extra quiere añadir? (peperoni, jamon, salmon):\n")
    if ingrediente_extra == "peperoni":
        print(f"La pizza elegida es vegetariana además lleva {ingrediente_extra}, mozzarella y tomate.")
    elif ingrediente_extra == "jamon":
        print(f"La pizza elegida es vegetariana además lleva {ingrediente_extra}, mozzarella y tomate.")
    elif ingrediente_extra == "salmon":
        print(f"La pizza elegida es vegetariana además lleva {ingrediente_extra}, mozzarella y tomate.")
    else:
        print("No se puede introducir ese ingrediente")
else:
    print("Esa pizza no existe.")
    