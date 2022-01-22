"""
Ejercicio 01
Descargar una copia del archivo "romeo.txt" desde
http://www.pythonlearn.com/code3/romeo.txt. Escribir un programa para abrir el
fichero y leerlo línea a línea. Por cada línea separar las palabras en una
lista de palabras usando la función split. Las palabras no deben estar
repetidas en la lista. Cuando la lista esté completa, visualizar el resultado
en orden alfabético.

>>> fichero ="C:/Users/migue/Documents/MEGA/Datos/Python/listas/romeo.txt"
>>> separaPalabras(fichero)
['already', 'and', 'arise', 'breaks', 'but', 'east', 'envious', 'fair', 'grief', 'is', 'it', 'juliet', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'who', 'window', 'with', 'yonder']

"""

import doctest


def separaPalabras(fichero):
    try:
        ficheroAbierto = open(fichero)
        
    except:
        print("No se encuentra el fichero")
        exit()

    salida = []
    linea = None
    for i in ficheroAbierto:
        linea = i.split(" ")
        for j in linea:
            if j in salida:
                continue
            else:
                palabra = j.rstrip("\n").lower()
                salida.append(palabra)
    salida2 = sorted(salida)
    return salida2

if __name__ == "__main__":
    import doctest
    doctest.testmod()