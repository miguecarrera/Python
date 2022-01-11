"""
Ejercicio 01c
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
c) Retorne dicha cadena cada dos caracteres. Ej.: "recta" imprime "rca"
### TESTS

>>> cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
>>> cad2(cad)
'E nlgrd aMnh ecy oben ueoaodre'

>>> cad3 = "recta"
>>> cad2(cad3)
'rca'

"""

def cad2(cadena):
    cad = ""
    for i in range(0,len(cadena),2):
        cad += cadena[i]

    return cad


if __name__ == "__main__":
    import doctest
    doctest.testmod()