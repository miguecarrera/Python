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

"""

def replace(cad, car=""):
    return cad.replace(" ",car)

if __name__ == "__main__":
    import doctest
    doctest.testmod()