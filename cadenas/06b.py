"""
Ejercicio 6b
Escribir funciones que dada una cadena de caracteres:
b) Devuelva solamente las letras vocales. Por ejemplo, si recibe "sin
consonantes" debe devolver "i ooae".
### TESTS

>>> cad = "sin consonantes"
>>> vocales(cad)
'i ooae'


>>> vocales(" ")
''
"""


def vocales(cad):
    salida = ""
    vocales = ["a", "e","i","o","u"]
    vocalesMayus = ["A","E","I","O","U"]
    if cad == " ":
        return salida
    else:
        for letra in cad:
            if letra in vocales or letra in vocalesMayus or letra == " ":
                salida += letra
            