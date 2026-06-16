#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Tema:a) Escribe un programa que solicite al usuario un número entero. 
#El programa debe determinar e imprimir si el número es "Positivo", "Negativo" o "Cero". Además,
#  si es diferente de cero, debe indicar si es "Par" o "Impar"
''
# Solicitar datos al usuario
numero = int(input("Ingrese un número entero: "))

# Determinar si es Positivo, Negativo o Cero
if numero > 0:
    print("El número es: Positivo")
elif numero < 0:
    print("El número es: Negativo")
else:
    print("El número es: Cero")

# Si es diferente de cero, verificar si es Par o Impar usando el residuo (%)
if numero != 0:
    if numero % 2 == 0:
        print("Además, es un número: Par")
    else:
        print("Además, es un número: Impar") 