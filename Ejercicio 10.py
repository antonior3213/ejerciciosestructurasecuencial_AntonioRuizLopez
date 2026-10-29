primera_calificacion = float(input("Ingrese la primera calificacion: "))
segunda_calificacion = float(input("Ingrese la segunda calificacion: "))
tercera_calificacion = float(input("Ingrese la tercera calificacion: "))
calificacion_examen_final = float(input("Ingrese la calificacion del examen final: "))
calificacion_trabajo_final = float(input("Ingrese la calificacion del trabajo final: "))

promedio_notas = (primera_calificacion + segunda_calificacion + tercera_calificacion) / 3
nota_fin = promedio_notas * 0.55 + calificacion_examen_final * 0.30 + calificacion_trabajo_final * 0.15

print("Tu nota final es:", nota_fin)