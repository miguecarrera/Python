"""
Ejercicio 2
===========
Escribir un programa que cuente la distribución horaria para el conjunto
de los mensajes. Se debe extraer la hora desde la línea "From" buscando
la cadena de tiempos y separándola en partes usando el caracter ":". Una
vez que se hayan acumulado la cuenta para cada hora, visualizar el
resultado, una por cada línea, ordenada por hora.
"""

try:
    fichero = open("C:/Users/migue/Documents/MEGA/Datos/Python/Diccionario/mbox-short.txt")
except IOError:
    print("No existe el archivo")

horas = dict()
lista_horas = []

for linea in fichero:
    if linea.startswith("From "):
        hora = linea.split()[5].split(":")[0]
        horas[hora] = horas.get(hora,0) + 1

for hora, count in list(horas.items()):
    lista_horas += [(hora, count)]

lista_horas.sort()
    

for hora, count in lista_horas:
    print(hora, " : ", count)