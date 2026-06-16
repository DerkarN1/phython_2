#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Escribe un algoritmo que permita al profesor ingresar las notas finales de sus estudiantes una por una. Para finalizar la entrada de notas finales,
# el profesor debe escribir -1. Durante la captura, si se introduce una nota inválida (menor que 0 o mayor que 50), el programa debe ignorar ese número,
# mostrar una alerta y continuar pidiendo la siguiente nota sin interrumpir el proceso. Al terminar, calcula la sumatoria y el promedio general de las notas válidas.

sumatoria_notas = 0
cantidad_notas = 0

print("Ingrese las notas finales de los estudiantes (Rango: 0 a 50).")
print("Para terminar de ingresar, escriba -1.")

while True:
    nota = float(input("Ingrese nota: "))
    
    if nota == -1:
        break
        
    if nota < 0 or nota > 50:
        print("¡Alerta! Nota inválida (Debe estar entre 0 y 50). Esta nota será ignorada.")
        continue  
        
    sumatoria_notas += nota
    cantidad_notas += 1

if cantidad_notas > 0:
    promedio = sumatoria_notas / cantidad_notas
    print("\n--- RESULTADOS FINALES ---")
    print(f"Cantidad de notas válidas ingresadas: {cantidad_notas}")
    print(f"Sumatoria total: {sumatoria_notas:.2f}")
    print(f"Promedio general del grupo: {promedio:.2f}")
else:
    print("No se registraron notas válidas para calcular el promedio.")

