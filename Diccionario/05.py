"""
Ejercicio 5
===========
En esta ocasión hay que registrar el nombre de dominio (en lugar de la
dirección), es decir, desde dónde se enviaron los mensajes en lugar de
de quién vino. Al final mostrar el contenido del diccionario.
"""

try:
    fichero = open("C:/Users/migue/Documents/MEGA/Datos/Python/Diccionario/mbox-short.txt")
except IOError:
    print("No existe el archivo")

dominios = dict()

for linea in fichero:
    if linea.startswith("From "):
        dominio = linea.split()[1].split("@")[1]
        dominios[dominio] = dominios.get(dominio,0) + 1

for linea in dominios:
    print(dominio, " : ", dominios[dominio])