"""
Ejercicio 01
Escribir un programa que lea las palabras de un fichero words.txt
(http://www.pythonlearn.com/code3/words.txt) y las almacene como claves en un
diccionario. No importan los valores.
Posteriormente leer palabras desde teclado y utilizar el operador in como una
forma rápida de comprobar si las palabras están dentro del diccionario o no.

>>> buscarPalabras("C:/Users/Miguel/Documents/miguel/Python/Diccionario/words.txt")
True

>>> buscarPalabras("C:/Users/Miguel/Documents/miguel/Python/Diccionario/words.txt")
False

"""




def buscarPalabras(fichero):
    try:
        ficheroAbierto = open(fichero)
    except IOError:
        return ("No existe ese fichero")

    texto = ficheroAbierto.read()
    ficheroAbierto.close()
    palabras = texto.split()
    diccionario = dict()
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1

    palabraIntro = input()
    if palabraIntro in diccionario:
        return True
    else:
        return False
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()