monto = float(input("Ingrese el monto de la fianza: "))

if monto < 5000000:
    cuota = monto * 0.03
else:
    cuota = monto * 0.02

print("La cuota a pagar es:", cuota)