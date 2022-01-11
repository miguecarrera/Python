"""
Ejercicio 01a
Escribir funciones que dada una cadena de caracteres:
a) Retorne los dos primeros caracteres.

###TEST
>>> cad = "Esto es una cadena"
>>> dos(cad)
'Es'

>>> cad2 = "Hola mundo"
>>> dos(cad2)
'Ho'

"""

def dos(cadena):
    return cadena[:2]

if __name__ == "__main__":
    import doctest
    doctest.testmod()