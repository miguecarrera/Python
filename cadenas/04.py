"""
Ejercicio 4
Escribir una función que reciba una cadena que contiene un largo número entero
y devuelva una cadena con el número y las separaciones de miles. Por ejemplo,
si recibe 1234567890, debe devolver 1.234.567.890
### TESTS

>>> cad = "1234567890"
>>> miles(cad)
'1.234.567.890'

>>> cad2 = "45612"
>>> miles(cad2)
'45.612'

"""

from pydoc import doc


def miles(cad):
    salida = ""
    contador = 0
    puntos = 0
    for i in range(0,len(cad)):
        salida += cad[len(cad)-1-i]
        contador += 1
        if (contador-puntos) == 3 or contador == 3:
            salida += "."
            puntos = contador 
    return salida[::-1]


if __name__=="__main__":
    import doctest
    doctest.testmod()