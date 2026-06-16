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
