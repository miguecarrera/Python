"""
Ejercicio 6
Reescribir el programa que solicita al usuario una lista de número y muestra
el valor máximo y mínimo de entre ellos y acaba con la palabra "done". Hacerlo
ahora almacenando los números en una lista y hacer uso de la funciones max() y
min().

>>> lista = [1,5,2,7,9,84,36,45,87,56]
>>> numeros(lista)
(87, 1)

>>> introducirNumeros()
(85.0, -1.0)

"""




def numeros(lista):
    return max(lista), min(lista)


def introducirNumeros():
    lista = list()
    done = False
    while not done:
        reading = True
        while reading:
            numero = input()
            #numero = input("Introduce un número, escriba fin para finalizar : ")
            if numero == "fin":
                done = True
                break
            try:
                numero = float(numero)
                reading = False
            except:
                #print("Entrada incorrecta, introduzca un número")
                continue
            lista.append(numero)
    return numeros(lista)



if __name__ == "__main__":
    import doctest
    doctest.testmod()