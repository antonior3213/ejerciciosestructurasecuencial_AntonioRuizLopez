sueldo_base = float(input("Introduce el sueldo base: "))
n = int(input("Numero de ventas: "))

suma = 0
for i in range(n):
    venta = float(input(f"Importe de la venta {i + 1}: "))
    suma = suma + venta

comision = suma * 0.10
total = sueldo_base + comision

print("Comision:", comision)
print("Total del mes:", total)