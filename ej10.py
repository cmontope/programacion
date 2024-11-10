

# 10.A ciertos estudiantes se les dice que su calificación final será el promedio
# de las dos calificaciones más altas de entre las tres que se han obtenido en
# el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo
# correspondiente a su nota final.

cal1 = 3.9
cal2 = 4.7
cal3 = 3.0


if cal1 <= cal2 and cal1 <= cal3:
        
        promedio = (cal2 + cal3) / 2

elif cal2 <= cal1 and cal2 <= cal3:
        
        promedio = (cal1 + cal3) / 2
else:
        
        promedio = (cal1 + cal2) / 2
    
print("La calificación final es:", promedio)