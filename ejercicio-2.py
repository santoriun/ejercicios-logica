"""
Escribe una función llamada analizar_frecuencia(texto) que reciba una cadena de texto y devuelva un diccionario con la cantidad de veces que aparece cada carácter.
"""
def analizar_frecuencia(texto) -> dict:
    dict_caracter = {}
    texto = texto.lower()
    texto = texto.replace(" ", "")

    for i in texto:
        if i not in dict_caracter:
            dict_caracter[i] = 1
        else:
            dict_caracter[i]+=1

    return dict_caracter

print(analizar_frecuencia("Hola mundo mi nombre es juan"))