sueldo = float(input("Ingrese el sueldo base: "))
venta = float(input("Ingrese el valor de la venta: "))

if venta < 100000:
    comision = venta * 0.10
else:
    comision = venta * 0.15

sueldo_total = sueldo + comision

print("Comision:", comision)
print("Sueldo a pagar:", sueldo_total)