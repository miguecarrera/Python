"""
Ejercicio 1
Revisar un programa previo de la siguiente forma: Leer y analizar
las líneas "From" y extraer las direcciones de la línea. Contar el
número de mensajes de cada persona usando un diccionario. Después
de leer todos los datos, crear una lista de tuplas de la forma
(contador, correo) desde el diccionario, ordenarla en orden inverso
y mostrar la persona con mayor número de envíos.
"""

try:
    fichero = open("C:/Users/migue/Documents/MEGA/Datos/Python/Diccionario/mbox-short.txt")
except IOError:
    print("No existe el archivo")

mails = dict()
lista_tupla = []

for linea in fichero:
    if linea.startswith("From "):
        linea = linea.split()
        mails[linea[1]] = mails.get(linea[1],0) + 1

for email, count in list(mails.items()):
    lista_tupla += [(email, count)]

lista_tupla.sort(reverse=True)
    

print(f"El email con mayor envío fue {lista_tupla[0][0]}")