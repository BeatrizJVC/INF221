import random

def matriz_aleatoria(filas, columnas, valor_min, valor_max):
    return [[random.randint(valor_min, valor_max) for _ in range(columnas)] for _ in range(filas)]

filas1=int(input("Ingrese el numero de filas: "))
columnas1 =int(input("Ingrese el numero de columnas: "))
valor_min1=int(input("Ingrese el valor minimo: "))
valor_max1=int(input("Ingrese el valor maximo: "))

lista1 = matriz_aleatoria(filas1,columnas1,valor_min1,valor_max1)

def guardar(lista_a, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Matriz =\n")
        for elemento1 in lista_a:
            archivo.write(f"{elemento1}\n")

guardar(lista1,"Matriz.txt")
