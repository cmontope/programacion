
#3.desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica
# un aumento del 15% si su sueldo es inferior a $300.000.
#

sueldo = float(input("Ingrese el sueldo del trabajador: "))

if sueldo < 300000:
    sueldo += sueldo * 0.15

print("El sueldo final es:", sueldo)