#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Tema: c) Solicita al usuario las longitudes de tres lados de un triángulo.
# Primero, verifica si con esas medidas se puede formar un triángulo 
#(la suma de dos lados cualesquiera siempre debe ser mayor que el tercero).
# Si es válido, clasifícalo en "Equilátero" (3 lados iguales),
# "Isósceles" (2 iguales) o "Escaleno" (todos diferentes)

# Entrada de los tres lados
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Validación de la existencia matemática del triángulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Las medidas forman un triángulo válido.")
    
    # Clasificación según la igualdad de sus lados
    if lado1 == lado2 and lado2 == lado3:
        print("Tipo de triángulo: Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo de triángulo: Isósceles")
    else:
        print("Tipo de triángulo: Escaleno")
else:
    print("Error: Con estas medidas NO se puede formar un triángulo.")