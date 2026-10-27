import math

numero1 = float(input("Escribe un número: "))
numero2 = float(input("Escribe otro número: "))

suma = numero1 + numero2
resto = numero1 - numero2
multiplicacion = numero1 * numero2

print(f"La suma de {numero1} y {numero2} es {suma}")
print(f"La resta de {numero1} y {numero2} es {resto}")
print(f"La multiplicación de {numero1} y {numero2} es {multiplicacion}")

if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} y {numero2} es {division}")
else:
    print("No se puede dividir entre cero.")
