import numpy as np

def matriz_orden(filas, columnas, tipo_orden='aleatorio'):
    matriz = np.random.randint(0, 100, size=(filas, columnas))
    
    if tipo_orden == 1:
        return matriz
    elif tipo_orden == 2:
        return np.sort(matriz, axis=1)
    elif tipo_orden == 3:
        num_filas_a_ordenar = filas // 2
        for i in range(num_filas_a_ordenar):
            matriz[i] = np.sort(matriz[i])
        return matriz
    elif tipo_orden == 4:
        for fila in matriz:
            mitad = len(fila) // 2
            fila[:mitad] = np.sort(fila[:mitad])
        return matriz
    else:
        raise ValueError("Tipo de ordenación no reconocido")

filas1=int(input("Ingrese el numero de filas: "))
columnas1 =int(input("Ingrese el numero de columnas: "))
orden1=int(input("Ingrese el tipo de ordenación 1 ('1.aleatorio', '2.completamente_ordenado', '3.semi_ordenado', '4.parcialmente_ordenado'): "))

lista1 = matriz_orden(filas1,columnas1,orden1)

def guardar(lista_a, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Matriz =\n")
        for elemento1 in lista_a:
            archivo.write(f"{elemento1}\n")

guardar(lista1,"Matriz.txt")
