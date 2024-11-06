# 7. Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo,
# el estado civil de cualquier persona e imprima el nombre de la persona, si
# corresponde a un hombre casado mayor de 40 años o a una mujer soltera
# menor de 50 años



nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))
sexo = input("Ingrese el sexo de la persona (M para masculino, F para femenino): ").upper()
estadoCivil = input("Ingrese el estado civil de la persona (casado/soltero): ").lower()

if (sexo == 'M' and estadoCivil == "casado" and edad > 40) or \
   (sexo == 'F' and estadoCivil == "soltero" and edad < 50):
    print("Nombre de la persona:", nombre)