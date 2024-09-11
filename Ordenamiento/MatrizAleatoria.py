import random

def matriz_aleatoria():
    filas=int(input("Ingrese el numero de filas: "))
    columnas =int(input("Ingrese el numero de columnas: "))
    valor_min=int(input("Ingrese el valor minimo: "))
    valor_max=int(input("Ingrese el valor maximo: "))
    lista = [[random.randint(valor_min, valor_max) for _ in range(columnas)] for _ in range(filas)]
    with open("Matriz.txt", 'w') as archivo:
        archivo.write("Matriz =\n")
        for elemento1 in lista:
            archivo.write(f"{elemento1}\n")
    return lista
