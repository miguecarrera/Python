"""
Ejercicio 02b
Escribir funciones que dada una cadena y un carácter:
b) Reemplace todos los espacios por el carácter. Ej: mi archivo de texto.txt y
_ debería devolver mi_archivo_de_texto.txt
### TESTS

>>> cad = "mi archivo de texto.txt"
>>> car = "_"
>>> replace(cad, car)
'mi_archivo_de_texto.txt'

>>> cad2 = "hola mundo"
>>> replace(cad2)
'holamundo'

>>> cad = "mi archivo de texto.txt"
>>> replace_2(cad, 200 , car)
'mi_archivo_de_texto.txt'

>>> cad = "mi archivo de texto.txt"
>>> replace_2(cad, 1 , car)
'mi_archivo de texto.txt'
"""

def replace(cad, car=""):
    return cad.replace(" ",car)

def replace_2(cad, num, car=""):
    contador = 0
    salida = ""
    for letra in cad:
        if contador >= num:
            salida += letra
        else:
            if letra == " ":
                salida += car
                contador += 1
            else:
                salida += letra

    return salida

if __name__ == "__main__":
    import doctest
    doctest.testmod()