"""
Ejercicio 02b
Escribir funciones que dada una cadena y un carácter:
c) Reemplace todos los dígitos en la cadena por el carácter "X".
Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
### TESTS

>>> cad = "4563"
>>> replace(cad)
'XXXX'

>>> cad2 = "4567"
>>> replace(cad2)
'XXXX'

>>> cad = "4568"
>>> replace_2(cad, 2)
'XX68'

>>> cad = "4568"
>>> replace_2(cad, 30)
'XXXX'

>>> cad = "4568"
>>> replace_2(cad, 3)
'XXX8'
"""

def replace(cad):
    salida = ""
    for i in range(0,len(cad)):
        salida += "X"

    return salida

def replace_2(cad, num):
    salida = ""
    contador = 0
    for i in range(0,len(cad)):
        if contador >= num:
            salida += cad[i]
        else:
            salida += "X"
            contador += 1

    return salida

if __name__=="__main__":
    import doctest
    doctest.testmod()