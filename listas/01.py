"""
Ejercicio 01
Descargar una copia del archivo "romeo.txt" desde
http://www.pythonlearn.com/code3/romeo.txt. Escribir un programa para abrir el
fichero y leerlo línea a línea. Por cada línea separar las palabras en una
lista de palabras usando la función split. Las palabras no deben estar
repetidas en la lista. Cuando la lista esté completa, visualizar el resultado
en orden alfabético.
"""

try:
    fichero = open('C:/Users/Miguel/Desktop/py/Python/listas/romeo.txt')
    
except:
    print("No se encuentra el fichero")
    exit()

salida = []
linea = None
for i in fichero:
    linea = i.split(" ")
    for j in linea:
        if j in salida:
            continue
        else:
            palabra = j.rstrip("\n").lower()
            salida.append(palabra)
salida2 = sorted(salida)
print(salida2)