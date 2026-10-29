minutos = int(input("Ingrese la cantidad de minutos: "))

res_horas = minutos // 60
res_minutos = minutos % 60
print(res_horas, "horas y", res_minutos, "minutos")