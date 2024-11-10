# 9. Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los
# ordene de mayor a menor e imprímalos.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))


if a > b and a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
elif b > a and b > c:
        if a > c:
            print(b, a, c)
        else:
            print(b, c, a)
elif c > a and c > b:
        if a > b:
            print(c, a, b)
        else:
            print(c, b, a)