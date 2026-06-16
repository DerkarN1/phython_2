#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Texto:d) Contador de Vocales. Pide al usuario que introduzca una frase o palabra. Utilizando un WHILE,
#recorre el texto y cuenta cuántas vocales que contiene en total, sin importar si están en mayúsculas o minúsculas. 

frase = input("inseretar la frace :" )

frase_minuscula = frase.lower()

vocales = "aeiouáéíóú"

contador_vocales = 0
letra = 0

while letra < len(frase_minuscula):
    letra_actual = frase_minuscula[letra]
    vocal = 0  
    es_vocal = False
    while vocal < len(vocales):
        if letra_actual == vocales[vocal]:
            es_vocal = True
            break
        vocal += 1
    if es_vocal:
        contador_vocales += 1
        
    letra += 1
print(f"La frase contiene un total de {contador_vocales} vocales.")