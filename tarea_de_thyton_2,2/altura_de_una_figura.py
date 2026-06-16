#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Solicita al usuario un número entero que representará la altura de una figura. 
#El programa debe imprimir en la consola un triángulo rectángulo hecho de asteriscos (*).
#Por ejemplo, si el usuario ingresa 4, la salida debe ser:

altura = int(input("Ingrese la altura de la figura: "))

for fila in range(1, altura + 1):
    
    for asterisco in range(fila):
        print("*", end="")  
    print()  
    