#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Tema:Desarrolla un sistema de venta de entradas para un cine. El programa debe pedir la edad del cliente y si posee una tarjeta de membresía estudiantil (Sí/No).
# La tarifa normal es de $8.00. Si es menor de 12 años, paga $4.00. Si tiene entre 12 y 18 años y es estudiante, recibe un 20% de descuento sobre la tarifa normal. 
#Si tiene más de 60 años, paga $5.00. Calcula y muestra el precio final.

edad = int(input("ingrese su edad :",))

estudiante = input("ingrese si es estudiante  :",)

tarjeta = input("ingrese si tiene tarjeta de menbresia :",)

tarifa = 8.00
descuento = 20
if edad < 12 :
    print('tiene que pagar 4.00$')
elif edad > 60 :
    print('tiene que pagra 5,00$')
elif edad >= 12 and edad <= 18 and (estudiante == "si" or estudiante == "si") :
    print("el valor a pagar:" , tarifa - (tarifa * descuento)/100)
else:
    print(f"tienes que pagar {tarifa}") 