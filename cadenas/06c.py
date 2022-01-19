"""
Ejercicio 6c
Escribir funciones que dada una cadena de caracteres:
c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe
'vestuario' debe devolver 'vistaerou'.
### TESTS

>>> cad = "vestuario"
>>> cambiarVocales(cad)
'vistaerou'

>>> cambiarVocales(" ")
''

>>> cad2 = "vIoLonchElO"
>>> cambiarVocales(cad2)
'vOuLunchIlU'

"""

from pydoc import doc


def cambiarVocales(cad):
    salida = ""
    vocales = "aeiou"
    vocalesMayus = "AEIOU"
    if cad == " ":
        return salida
    else:
        for letter in cad:
            if letter in vocales:
                try:
                    n = vocales[vocales.find(letter)+1]
                    salida += n
                except:
                    n = vocales[0]
                    salida += n
            elif letter in vocalesMayus:
                try:
                    n = vocalesMayus[vocalesMayus.find(letter)+1]
                    salida += n
                except:
                    n = vocalesMayus[0]
                    salida += n
            else:
                salida += letter
    
    return salida



if __name__ == "__main__":
    import doctest
    doctest.testmod()