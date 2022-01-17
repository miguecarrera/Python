"""
Ejercicio 5a
Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial
Bus debe devolver USB.
### TESTS

>>> cad = "Universal Serial Bus"
>>> siglas(cad)
'USB'

>>> cad2 = "Random Access Memory"
>>> siglas(cad2)
'RAM'

>>> cad3 = " "
>>> siglas(cad3)
' '

"""

def siglas(cad):
    if cad == " ":
        return cad
    salida = ""
    cadena = cad.split(" ")
    for i in cadena:
        salida += i[0]
    return salida


if __name__ == "__main__":
    import doctest
    doctest.testmod()