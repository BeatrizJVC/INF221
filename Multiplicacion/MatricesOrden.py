import numpy as np

def matriz_orden():
    filas=int(input("Ingrese el numero de filas: "))
    columnas =int(input("Ingrese el numero de columnas: "))
    tipo_orden=int(input("Ingrese el tipo de ordenación (1. Aleatorio, 2. Completamente ordenado, 3. Semi ordenado, 4. Parcialmente ordenado): "))

    matriz = np.random.randint(0, 100, size=(filas, columnas))

    if tipo_orden == 1:
        lista = matriz
    elif tipo_orden == 2:
        lista = np.sort(matriz, axis=1)
    elif tipo_orden == 3:
        num_filas_a_ordenar = filas // 2
        for i in range(num_filas_a_ordenar):
            matriz[i] = np.sort(matriz[i])
        lista = matriz
    elif tipo_orden == 4:
        for fila in matriz:
            mitad = len(fila) // 2
            fila[:mitad] = np.sort(fila[:mitad])
        lista = matriz
    else:
        raise ValueError("Tipo de ordenación no reconocido")
    return lista

def crear_matrices_o():
    print("Caracteristicas matriz 1:")
    lista1 = matriz_orden()
    print("\nCaracteristicas matriz 2:")
    lista2 = matriz_orden()
    return [lista1, lista2]

def matrices_orden():
    listas=crear_matrices_o()
    lista_a = listas[0]
    lista_b = listas[1]
    with open("Matrices.txt", 'w') as archivo:
        archivo.write("Matriz 1 =\n")
        for elemento1 in lista_a:
            archivo.write(f"{elemento1}\n")

        archivo.write("\n\nMatriz 2 =\n")
        for elemento2 in lista_b:
            archivo.write(f"{elemento2}\n")
    return listas
