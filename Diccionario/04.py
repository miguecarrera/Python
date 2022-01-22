"""
Ejercicio 4
===========
Añadir código al programa anterior para averiguar quién tiene más mensajes en
el fichero.
Después de leer todos los datos y esté creado el diccionario buscar a través
de él, usando un bucle máximo (ver la sección
[https://books.trinket.io/pfe/05-iterations.html] maximumloop) para
encontrar quién tiene más mensajes y mostrar en pantalla cuántos mensajes
tenía esa persona.
"""

try:
    fichero = open("C:/Users/migue/Documents/MEGA/Datos/Python/Diccionario/mbox-short.txt")
except IOError:
    print("No existe el archivo")

mail = dict()

for linea in fichero:
    if linea.startswith("From "):
        linea = linea.split()
        mail[linea[1]] = mail.get(linea[1],0) + 1

max = 0
max_email = ""

for email in mail:
    if mail[email] > max:
        max = mail[email]
        max_email = email

print(max_email, " : ", max)