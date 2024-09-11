def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

def optimizado(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    
    if columnas1 != filas2:
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
    
    matriz2_transpuesta = transponer_matriz(matriz2)
    
    resultado = [[0] * columnas2 for _ in range(filas1)]
    
    for i in range(filas1):
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1):
                suma += matriz1[i][k] * matriz2_transpuesta[j][k]
            resultado[i][j] = suma
    
    return resultado
