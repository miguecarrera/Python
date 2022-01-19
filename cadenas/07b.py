"""
Ejercicio 7a
Escribir funciones que dadas dos cadenas de caracteres:
b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe
"kde" y "gnome" debe devolver "gnome".
### TESTS

>>> anterior("kde","gnome")
'gnome'


>>> anterior(" ", "hola")
'hola'

>>> anterior("hola","holo")
'hola'
"""

def anterior(cad, cad2):
    cad = cad.lower()
    cad2 = cad2.lower()
    for i,j in cad,cad2:
        if i < j or j == " ":
            return cad
        elif i > j or i == " ":
            return cad2