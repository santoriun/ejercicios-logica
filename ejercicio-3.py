# palabra palindroma.
import string
def es_palindroma(texto : str) -> bool:

    # limpieza de texto.
    texto_limpio = texto.lower().replace(" ", "")
    remplazo_tildes={
        "á": "a",
        "é": "e", 
        "í": "i",
        "ó": "o", 
        "ú": "u"
    }
    for con_tilde, sin_tilde in remplazo_tildes.items():
        texto_limpio=texto_limpio.replace(con_tilde,sin_tilde)
    
    tabla_limpieza = str.maketrans("","",string.punctuation+"¡¿")
    texto_limpio=texto_limpio.translate(tabla_limpieza)

    # Retroceso de la frase o palabra.
    texto_inverso = texto_limpio[::-1]

    # Validacion.
    if texto_limpio == texto_inverso:
        return True
    else:
        return False
    

print(es_palindroma("Aníta láva!!! la tina"))