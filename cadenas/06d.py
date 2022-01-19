"""
Ejercicio 6d
Escribir funciones que dada una cadena de caracteres:
d) Indique si se trata de un palíndromo. Por ejemplo, anita lava la tina es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
### TESTS

>>> palindromo("el bar es iman o zona miserable")
True

>>> palindromo("hola mundo")
False

>>> palindromo("Ana")
True

"""

def palindromo(cad):
    reverse = cad[::-1]
    reverse = reverse.replace(" ","").lower()
    cad = cad.replace(" ","").lower()

    if cad == " ":
        return False
    elif cad == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()