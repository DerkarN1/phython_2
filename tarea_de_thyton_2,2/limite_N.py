#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Tema:Desarrolla un programa que pide un número que indica el límite superior N. Utilizando un bucle for,
#calcula la suma de todos los números impares que se encuentran en el rango desde 1 hasta N. Al final,
#muestra la cantidad de números procesados, y el resultado de la sumatoria. 

numero_N = int(input("insete su numero: "))
sumatoria = 0
numero_impar = 0
for i in range(1,numero_N+1):
    if i % 2 == 0:
      sumatoria+=i
      numero_impar+= 1
print(f"Cantidad de números impares: {numero_impar}")
print(f"El resultado de la sumatoria es: {sumatoria}")
