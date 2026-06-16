#fecha: 2024-06-13
#Tema:operaciones aritméticas
# Autor: Bryan Adriano Nazareno Quinonez

print("La suma de 8 + 9",8+9)
print("El producto de 8 x 9",8*9)
print("El cociente de 100 / 3",100/3)
print("El residuo  de 100 % 3",100%3)
print("Potencia: 4 al cubo es ",4**7)
print("Division entera 17 div 3 es ",17//3)

#imprecion de tipos de datos en Phython 
print("El tip de dato del 9 es : " , type(9))
print("El tipo de dato del 5.55 es:" , type(5.55))
print("El tipo de dato de la patabra PUSECE es:" , type("PUSECE")) 
print("El tipo de dato de booleano True es:" , type(True))
print("El tipo de dato de la siguiente lista [1,2,3,4] es:" , type([1,2,3,4]))
print("El tipo de dato de la siguiente lista [casa,mesa,silla] es:" , type(["casa","mesa","silla"]))


info_personal = {
    "Apellido" : "Ponce",
    "Nombre" : "Juan",
    "Edad" : 22,
    "Sexo" : "Masculino",
} 

#declaracion de multiples variables en la misma linea 
libro, precio, autor, tienepaguinaWED = "EL Alquimista", 10.33, "Paulo Coelho", False
print("datos del libro")
print(f"Nombre{libro}")
print(f"Precio{precio}")
print(f"Autor{autor}")
print(f"tiene paginas{tienepaguinaWED}")

