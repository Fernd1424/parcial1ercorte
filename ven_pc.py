cantidad = int(input("Ingrese la cantidad de computadores: "))
precio = float(input("Ingrese el precio de cada computador: "))

compra = cantidad * precio

if cantidad < 5:
    descuento = compra * 0.10

elif cantidad < 10:
    descuento = compra * 0.20

else:
    descuento = compra * 0.30

pagar = compra - descuento

print("Valor de la compra:", compra)
print("Descuento:", descuento)
print("Valor a pagar:", pagar)