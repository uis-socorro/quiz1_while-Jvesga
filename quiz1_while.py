"""Calcular en cuanto tiempo Pedro y Juan pueden hacer el negocio"""

print("------------------------------------------------------------------------------------------")
print("---Calcular el numero de meses necesarios para que pablo y juan puedan hacer su negocio---")
print("------------------------------------------------------------------------------------------")

c1 = int(input("Digite el capital inicial de Juan: "))
c2 = int(input("Digite el capital inicial de Pablo:"))
c3 = int(input("Digite el valor del capital necesario para el negocio: "))
n = 0

while (c1 + c2) < c3:
    c1 = c1 + (c1 * 0.03)
    c2 = c2 + (c2 * 0.04)
    n = n + 1
    
print("Los mese necesarios para que Pablo y Juan puedan hacer el negocio son: " , str(n))