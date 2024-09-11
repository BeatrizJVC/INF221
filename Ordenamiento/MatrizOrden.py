import numpy as np

def matriz_orden():
    filas=int(input("Ingrese el numero de filas: "))
    columnas =int(input("Ingrese el numero de columnas: "))
    tipo_orden=int(input("Ingrese el tipo de ordenación 1 ('1.aleatorio', '2.completamente_ordenado', '3.semi_ordenado', '4.parcialmente_ordenado'): "))

    matriz = np.random.randint(0, 100, size=(filas, columnas))
    
    if tipo_orden == 1:
        lista=matriz
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
        
    with open("Matriz.txt", 'w') as archivo:
        archivo.write("Matriz =\n")
        for elemento1 in lista:
            archivo.write(f"{elemento1}\n")
    return lista
