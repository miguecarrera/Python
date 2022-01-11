"""
Ejercicio 01d
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
d) Retorne dicha cadena en sentido inverso.
Ej.: '¡Hola mundo!' debe imprimir '!odnum aloH¡'
### TESTS

>>> cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
>>> inversa(cad)
'emradroca oreiuq on erbmon oyuc ed ahcnaM al ed ragul nu nE'

>>> cad2 = "hola mundo"
>>> inversa(cad2)
'odnum aloh'

"""

def inversa(cad):
    return cad[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()