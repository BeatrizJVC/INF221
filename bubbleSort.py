def bubble_sort_matriz(matriz):
    for row in matriz:
        n = len(row)
        for i in range(n):
            for j in range(0, n-i-1):
                if row[j] > row[j+1]:
                    row[j], row[j+1] = row[j+1], row[j]
    return matriz