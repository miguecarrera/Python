fichero = open("C:/Users/Miguel/Desktop/py/Python/contar_faltas/pagina.html","w+")
salida = ""
for linea in fichero:
    salida += linea.strip("\n")
    fichero += fichero.write(salida)