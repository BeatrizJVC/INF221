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

filas1=int(input("Ingrese el numero de filas de la primera matriz: "))
columnas1 =int(input("Ingrese el numero de columnas de la primera matriz: "))
orden1=int(input("Ingrese el tipo de ordenación 1 ('1.aleatorio', '2.completamente_ordenado', '3.semi_ordenado', '4.parcialmente_ordenado'): "))

filas2=int(input("\nIngrese el numero de filas de la segunda matriz: "))
columnas2 = int(input("Ingrese el numero de columnas de la segunda matriz: "))
orden2=int(input("Ingrese el tipo de ordenación 2 ('1.aleatorio', '2.completamente_ordenado', '3.semi_ordenado', '4.parcialmente_ordenado'): "))

lista1 = matriz_orden(filas1,columnas1,orden1)
lista2 = matriz_orden(filas2,columnas2,orden2)

def guardar(lista_a, lista_b, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Matriz 1 =\n")
        for elemento1 in lista_a:
            archivo.write(f"{elemento1}\n")

        archivo.write("\n\nMatriz 2 =\n")
        for elemento2 in lista_b:
            archivo.write(f"{elemento2}\n")

guardar(lista1,lista2,"Matrices.txt")
