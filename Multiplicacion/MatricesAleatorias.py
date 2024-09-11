import random

def matriz_aleatoria():
    filas=int(input("Ingrese el numero de filas: "))
    columnas =int(input("Ingrese el numero de columnas: "))
    valor_min=int(input("Ingrese el valor minimo: "))
    valor_max=int(input("Ingrese el valor maximo: "))

    return [[random.randint(valor_min, valor_max) for _ in range(columnas)] for _ in range(filas)]

def crear_matrices_a():
    print("Caracteristicas matriz 1:")
    lista1 = matriz_aleatoria()
    print("\nCaracteristicas matriz 2:")
    lista2 = matriz_aleatoria()
    return [lista1, lista2]

def matrices_aleatorias():
    listas=crear_matrices_a()
    lista_a=listas[0]
    lista_b=listas[1]
    with open("Matrices.txt", 'w') as archivo:
        archivo.write("Matriz 1 =\n")
        for elemento1 in lista_a:
            archivo.write(f"{elemento1}\n")

        archivo.write("\n\nMatriz 2 =\n")
        for elemento2 in lista_b:
            archivo.write(f"{elemento2}\n")
    return listas
