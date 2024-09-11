import random

def matriz_aleatoria(filas, columnas, valor_min, valor_max):
    return [[random.randint(valor_min, valor_max) for _ in range(columnas)] for _ in range(filas)]

filas1=int(input("Ingrese el numero de filas de la primera matriz: "))
columnas1 =int(input("Ingrese el numero de columnas de la primera matriz: "))
valor_min1=int(input("Ingrese el valor minimo de la primera matriz: "))
valor_max1=int(input("Ingrese el valor maximo de la primera matriz: "))

filas2=int(input("\nIngrese el numero de filas de la segunda matriz: "))
columnas2 = int(input("Ingrese el numero de columnas de la segunda matriz: "))
valor_min2=int(input("Ingrese el valor minimo de la segunda matriz: "))
valor_max2=int(input("Ingrese el valor maximo de la segunda matriz: "))

lista1 = matriz_aleatoria(filas1,columnas1,valor_min1,valor_max1)
lista2 = matriz_aleatoria(filas2,columnas2,valor_min2,valor_max2)

def guardar(lista_a, lista_b, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Matriz 1 =\n")
        for elemento1 in lista_a:
            archivo.write(f"{elemento1}\n")

        archivo.write("\n\nMatriz 2 =\n")
        for elemento2 in lista_b:
            archivo.write(f"{elemento2}\n")

guardar(lista1,lista2,"Matrices.txt")
