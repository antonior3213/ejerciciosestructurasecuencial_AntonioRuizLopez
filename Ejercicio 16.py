d = float(input("Distancia entre los coches (km): "))
v1 = float(input("Velocidad del coche de atrás (km/h): "))
v2 = float(input("Velocidad del coche de delante (km/h): "))
acercamiento = v1 - v2
horas = d / acercamiento
minutos = horas * 60
print("El coche lo alcanza en", minutos, "minutos")
