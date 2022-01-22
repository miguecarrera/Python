"""
Ejercicio 02
Escribe un programa que contabilice cada mensaje de correo electrónico
por el día de la semana en que se envió. El proceso buscará líneas que
comiencen con "From " mirarán la tercera palabra de la línea y registrará
la cuenta para cada día de la semana. Al final del programa visualizar
los totales de cada día.
"""

try:
    fichero = open("Diccionario\mbox-short.txt")
except IOError:
    print("No existe el archivo")
    exit()

dias_semana = dict()

for linea in fichero:
    if linea.startswith("From "):
        dia = linea.split()[2]
        dias_semana[dia] = dias_semana.get(dia, 0) + 1

dia_es = ["Lunes", "Martes", "Miércoles", "Jueves","Viernes", "Sábado", "Domingo"]
dia_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for dia in range(7):
    if dia_en[dia] in dias_semana:
        print(f"{dia_es[dia]} : {dias_semana[dia_en[dia]]}")