"""
Ejercicio 02a
Escribir funciones que dada una cadena y un carácter:
a) Inserte el carácter entre cada letra de la cadena. Ej: separar y , debería
devolver s,e,p,a,r,a,r
### TESTS
>>> cad = "En un lugar de la Mancha"
>>> separar(cad)
'E,n, ,u,n, ,l,u,g,a,r, ,d,e, ,l,a, ,M,a,n,c,h,a'
>>> cad = "En"
>>> separar(cad)
'E,n'
"""


def separar(cad):
    salida = ""
    for letra in cad:
        salida += letra + ","
    return salida[:-1]



if __name__ == '__main__':
    import doctest
    doctest.testmod()