"""
Ejercicio 02d
Escribir funciones que dada una cadena y un carácter:
d) Inserte el carácter cada 3 dígitos en la cadena.
Ej. 2552552550 y . debería devolver 255.255.255.0
### TESTS

>>> cad = "2552552550"
>>> car = "."
>>> puntos(cad, car)
'255.255.255.0'

>>> cad = ""
>>> car = ""
>>> puntos(cad, car)
''

>>> cad = "25"
>>> car = "."
>>> puntos(cad, car)
'25'

>>> cad = "255"
>>> car = "."
>>> puntos(cad, car)
'255'

>>> cad ="255255255"
>>> car = "."
>>> num = 1
>>> puntos_2(cad, num, car)
'255.255255'

>>> cad ="255255"
>>> car = "."
>>> num = 5
>>> puntos_2(cad, num, car)
'255.255'

"""

def puntos(cad, car="."):
    salida=""
    puntos=0
    contador=0
    if(len(cad)<=3):
        return cad
    else:
        for i in range(0,len(cad)):
            if(i+1 > len(cad)):
                salida += cad[i]
                break
            else:
                if(contador - puntos == 3):
                    salida = salida + car + cad[i]
                    puntos = contador
                    contador += 1
                else:
                    salida += cad[i]
                    contador += 1
        return salida


def puntos_2(cad, num, car="."):
    n_puntos = 0
    salida=""
    puntos=0
    contador=0
    if(len(cad)<=3):
        return cad
    else:
        for i in range(0,len(cad)):
            if n_puntos < int(num):
                if(i+1 > len(cad)):
                    salida += cad[i]
                    break
                else:
                    if(contador - puntos == 3):
                        salida = salida + car + cad[i]
                        puntos = contador
                        contador += 1
                        n_puntos += 1
                    else:
                        salida += cad[i]
                        contador += 1
            else:
                salida += cad[i]
        return salida



if __name__ == "__main__":
    import doctest
    doctest.testmod()