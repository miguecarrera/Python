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

>>> cad = "En un lugar de la Mancha"
>>> separar_2(cad, 2)
'E,n, un lugar de la Mancha'

>>> cad = "En un lugar de la Mancha"
>>> separar_2(cad, 200)
'E,n, ,u,n, ,l,u,g,a,r, ,d,e, ,l,a, ,M,a,n,c,h,a'
"""


def separar(cad):
    salida = ""
    for letra in cad:
        salida += letra + ","
    return salida[:-1]

def separar_2(cad, num):
    salida = ""
    contador = 0
    for letra in cad:
        if(contador >= num):
            salida += letra
        else:
            salida += letra + ","
            contador+=1
    
    if(len(cad)< num):
        return salida[:-1]
    else:
        return salida




if __name__ == '__main__':
    import doctest
    doctest.testmod()