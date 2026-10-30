num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
if num1 > num2:
    distancia = num1 - num2
elif num2 > num1:
    distancia = num2 - num1
print("La distancia entre estos numeros es ", distancia)