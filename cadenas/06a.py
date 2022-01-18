"""
Ejercicio 6a
Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe
'Algoritmos o logaritmos' debe devolver 'lgrtms  lgrtms'.
### TESTS

>>> cad = "Algoritmos o logaritmos"
>>> consonante(cad)
'lgrtms  lgrtms'

>>> cad2 = " "
>>> consonante(cad2)
''

"""



def consonante(cad):
    salida = ""
    vocales = ["a","e","i","o","u"]
    vocalesMayus = ["A","E","I","O","U"]
    if cad == " ":
        return salida
    else:
        for i in cad:
            if i in vocales or i in vocalesMayus:
                continue
            else:
                salida += i
    return salida


if __name__ == "__main__":
    import doctest
    doctest.testmod()