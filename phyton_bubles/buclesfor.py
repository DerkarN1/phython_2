#fecha: 2024-06-13
#Tema:ejercicio al bucle for 
# Autor: Bryan Adriano Nazareno Quinonez

#for que se ejecuta del 0 al 4
for i in range(5):
    print("hola, el valor de i es :", i)
    print("=======")

print()
#el bucle recorre la lista 
ciudades = ["Esmeraldadad", "quito", "Protoviejo", "cuenca", "Ambato"]
print("Lista de ciudades del Ecuador:")
for ciudad in ciudades:
    print(ciudad)


#Recorre una cadena de caracteres
print()
palabra = "PUCe ESMERALDAS"

for letra in palabra:
    print(letra)


#Ejercicio: #1 Coentre  las letras "E" de la Puce Esmeraldas
cont = 0
for letra in palabra:
    if letra == "E" or letra ==  "e":
        cont = cont + 1
print (f"la cantidad de letas E en la palabra {palabra} es {cont} ")


# Ejercicio: #2
#dicenña buble que cuente la vocales que existen en una palabra. 
#palabra insertada por teclado.

vocales=""

vocales= input("inserta las palavra deceada:")

cont = 0
for vocal in vocales:
    if vocal =="A" or vocal ==  "a" or vocal ==  "E" or vocal ==  "e" or vocal ==  "I" or vocal ==  "i"  or vocal ==  "O" or vocal ==  "o"or vocal ==  "U"or vocal ==  "U":
        cont = cont + 1
print (f"la cantidad de vocales es {cont} ")


#for con rango 
print()
for i in range (1,11):
    print("El valor de i ", i)
 