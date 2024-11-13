# 17.desarrollar el algoritmo que lea tres números y diga si uno es divisible del otro

# Leer tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificar divisibilidad entre los números
if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} es divisible por {num2}")
else:
    print(f"{num1} no es divisible por {num2}")

if num3 != 0 and num1 % num3 == 0:
    print(f"{num1} es divisible por {num3}")
else:
    print(f"{num1} no es divisible por {num3}")

if num1 != 0 and num2 % num1 == 0:
    print(f"{num2} es divisible por {num1}")
else:
    print(f"{num2} no es divisible por {num1}")

if num3 != 0 and num2 % num3 == 0:
    print(f"{num2} es divisible por {num3}")
else:
    print(f"{num2} no es divisible por {num3}")

if num1 != 0 and num3 % num1 == 0:
    print(f"{num3} es divisible por {num1}")
else:
    print(f"{num3} no es divisible por {num1}")

if num2 != 0 and num3 % num2 == 0:
    print(f"{num3} es divisible por {num2}")
else:
    print(f"{num3} no es divisible por {num2}")
