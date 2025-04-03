# Una tienda ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por 
# la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia
# una unidad del producto por cada docena en exceso sobre 3. Diseñe un algoritmo que determine el monto de la 
# compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta
# cantidad de docenas del producto.

costo_por_unidad = int(input('Ingresa el costo por unidad: '))
docenas_del_producto = int(input('Ingresa la cantidad de docenas: '))
monto_compra = costo_por_unidad * docenas_del_producto * 12
if docenas_del_producto > 3:
    monto_descuento=monto_compra * 0.15
    obsequios = docenas_del_producto - 3
else:
    monto_descuento=monto_compra * 0.1
    obsequios = 0
monto_pagar=monto_compra-monto_descuento
print (f"Monto a pagar: {monto_pagar}")
print (f"Monto de la compra: {monto_compra}")
print (f"Monto del descuento: {monto_descuento}")
print (f"Número de obsequio: {obsequios}")