""""
Ejercicio 5c
Escribir una función que dada una cadena de caracteres, devuelva:
c) Las palabras que comiencen con la letra A. Por ejemplo, si recibe "Antes de
ayer" debe devolver "Antes ayer".
### TESTS

>>> cad = "Antes de ayer"
>>> fLetter(cad)
'Antes ayer'


>>> cad2 = "hola hasta mañana"
>>> fLetter(cad2)
''

>>> cad3 = " "
>>> fLetter(cad3)
''

"""

def fLetter(cad):
    salida = ""
    if cad == " ":
        return salida
    else:
        cadSep = cad.split(" ")
        for i in cadSep:
            if i[0] == "a" or i[0] == "A":
                salida += i + " "

    return salida.rstrip(" ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()