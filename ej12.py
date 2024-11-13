# 12.Un vendedor desea calcular su comisión total sobre las ventas de varios
# artículos. Al vendedor le corresponde el 3% de comisión sobre artículos
# cuyo precio es menor de $2.000 y el 5% de comisión sobre artículos
# cuyo precio es de $2000 o más. El vendedor hizo 50 ventas y desea
# saber también cuántas ventas hizo menores de 2000 y cuantas mayores o
# iguales a 2000.

# Lista de precios de las ventas
ventas = [2500, 1500, 3000, 1800, 2100, 2500, 1900, 2300, 2200, 2100,
          1700, 2000, 1500, 2100, 1800, 1900, 2000, 2100, 2000, 1600,
          1400, 2500, 1500, 1000, 2000, 1900, 2200, 2600, 1800, 3000,
          1700, 1200, 1500, 2100, 2600, 2300, 1800, 2200, 2000, 2100,
          1400, 2000, 2500, 1500, 2700, 1600, 1800, 2900, 1000, 2000]

# Variables para las comisiones y contadores
comision_total = 0
ventas_menores_2000 = 0
ventas_mayores_o_iguales_2000 = 0

# Calcular comisiones y contar ventas
for precio in ventas:
    if precio < 2000:
        comision_total += precio * 0.03
        ventas_menores_2000 += 1
    else:
        comision_total += precio * 0.05
        ventas_mayores_o_iguales_2000 += 1

# Resultados
print("Comisión total del vendedor: $", round(comision_total, 2))
print("Ventas menores de $2000:", ventas_menores_2000)
print("Ventas de $2000 o más:", ventas_mayores_o_iguales_2000)