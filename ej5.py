
# 5. desarrollar un programa que capture tres números e imprima por pantalla
# cual es el número mayor, el menor, cuales son iguales, si los tres
# diferentes.

# Captura de tres números ingresados por el usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Determinar el mayor y el menor
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Imprimir el mayor y el menor
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

# Comprobar si los números son iguales o diferentes
if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 != num2 != num3 != num1:
    print("Los tres números son diferentes.")
else:
    # Comprobar si hay dos números iguales
    if num1 == num2:
        print("El primer y segundo número son iguales.")
    if num1 == num3:
        print("El primer y tercer número son iguales.")
    if num2 == num3:
        print("El segundo y tercer número son iguales.")