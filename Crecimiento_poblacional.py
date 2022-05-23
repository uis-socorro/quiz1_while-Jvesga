"""CRECIMIENTO POBLACIONAL DE DOS CIUDADES"""




print("-------------------------------------------------------")
print("----Programa que calcula el crecimiento poblacional----")
print("-------------------------------------------------------")

N = int(1980)
A = float(3.5)
B = float(5)
while A < B:
    N = N + 1
    A = A + (A * 0.07)
    B = B + (B * 0.05)

print("En el año " , str(N) , "la ciudad A tendra una poblacion de " , str(A) , "millones de personas" , " y la ciudad B una poblacion de " , str(B), "millones de personas")