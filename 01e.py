"""
Ejercicio 01e
Escribir funciones que dada una cadena de caracteres:
e) Imprima la cadena en un sentido y en sentido inverso.
Ej: reflejo imprime reflejoojelfer.

#TESTS

>>> cad = "reflejo"
>>> reflejo(cad)
'reflejoojelfer'

>>> cad2 = "hola mundo"
>>> reflejo(cad2)
'hola mundoodnum aloh'

"""


def reflejo(cadena):
    return cadena + cadena[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()