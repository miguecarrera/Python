"""
Ejercicio 03
Escribir un programa que lea un log de correo construya un histograma usando
un diccionario para contar cuántos mensajes se recibieron de cada dirección
de correo electrónico y visualice los resultados.
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

for email in mail:
    print(email, " : ", mail[email])