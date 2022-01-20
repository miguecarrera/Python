"""
Ejercicio 02
Escribe un programa que lea del fichero de buzón de correo
mbox-short.txt (http://www.pythonlearn.com/code/mbox-short.txt) y cada vez que
se encuentre una línea que empiece por "From" separarla en palabras. Interesa
quién envió el mensaje (segunda palabra de la línea "From") sin la parte del
dominio. Es decir, de:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
mostraremos solo "stephen.marquard".
El programa debe mostrar la lista de los usuarios ordenada alfabéticamente,
sin repetir ninguno y finalizar visualizando el total de líneas encontradas.

>>> fichero = "C:/Users/Miguel/Documents/miguel/Python/listas/mbox-short.txt"
>>> usuario(fichero)
(11, 27)

>>> usuario("hola.txt")
'No existe el fichero'

"""

def usuario(fichero):
    try:
        ficheroAbierto = open(fichero)
    except IOError:
        return("No existe el fichero")

    usuarios = list()

    contador = 0

    for linea in ficheroAbierto:
        if linea.startswith("From "):
            contador += 1
            usuario = linea.split()[1].split('@')[0]
            if usuario not in usuarios:
                usuarios.append(usuario)

    usuarios.sort()

    return len(usuarios),contador
    #print(usuarios)
    #print(f"El numero de lineas encontradas es de {contador}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()