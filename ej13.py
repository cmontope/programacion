# 13.desarrollar un algoritmo que halle la nota total de una materia en el SENA, y
# determine si la gano o la reprobó

nota1 = float(input("Ingrese el valor de la primera nota: "))

nota2 = float(input("Ingrese el valor de la segunda nota: "))

nota3 = float(input("Ingrese el valor de la tercera nota: "))


promedioNotas = (nota1 + nota2 + nota3) / 3 

if promedioNotas >= 3 : 
    print("El alunmo Aprobo. " "La nota es: ", promedioNotas)
else: 
    print("El alumno reprueba. " "La nota es: ", promedioNotas)


