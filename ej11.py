# 11 .Escriba un algoritmo que acepte o rechace una pieza en forma de varilla,
# para una empresa de acuerdo a los siguientes criterios:
# a. Su longitud debe ser mayor de 7.5 cm pero no exceder los 9 cm
# b. Su diámetro no debe ser menor que 0.5 cm ni mayor de 1.3 cm.
# c. Por ningún motivo su masa debe exceder los 5.8 cm
# i. Nota: masa = diámetro * longitud / densidad; densidad = 3.5
# Gr/cm

def verificar_pieza(longitud, diametro):
    # Definir la densidad
    densidad = 3.5
    
    # Verificar que la longitud esté en el rango permitido
    if 7.5 < longitud <= 9:
        # Verificar que el diámetro esté en el rango permitido
        if 0.5 <= diametro <= 1.3:
            # Calcular la masa de la pieza
            masa = (diametro * longitud) / densidad
            
            # Verificar que la masa no exceda el límite permitido
            if masa <= 5.8:
                return "Pieza Aceptada"
            else:
                return "Pieza Rechazada: La masa excede el límite permitido"
        else:
            return "Pieza Rechazada: Diámetro fuera del rango permitido"
    else:
        return "Pieza Rechazada: Longitud fuera del rango permitido"

# Ejemplo de uso:
longitud = float(input("Ingrese la longitud de la pieza (cm): "))
diametro = float(input("Ingrese el diámetro de la pieza (cm): "))

resultado = verificar_pieza(longitud, diametro)
print(resultado)
