# 16.desarrollar un algoritmo que capture un número y diga si es par o impar.


numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero ingresado, ", numero, " es PAR")
else:
    print("El numero ingresado, ", numero, " es IMPAR")