x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

dx = x2 - x1
dy = y2 - y1

distancia = (dx * dx + dy * dy) ** 0.5

print("La distancia entre los puntos es ", distancia)