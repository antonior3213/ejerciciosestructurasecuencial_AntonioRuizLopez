n = int(input("Ingrese un numero de dos cifras: "))
unidades = n % 10
decenas = n // 10
invertido = (unidades * 10) + decenas
print(invertido)
