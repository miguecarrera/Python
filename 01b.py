"""
Ejercicio 01b
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
b) Imprima los tres últimos caracteres.

### TEST

>>> cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
>>> tres(cad)
'rme'

>>> cad2 = "Hola mundo"
>>> tres(cad2)
'ndo'

>>> cad3 = "Adios humanos"
>>> tres(cad3)
'nos'

"""

def tres(cadena):
    return cadena[-3:]

if __name__ == "__main__":
    import doctest
    doctest.testmod()