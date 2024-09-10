def insertion_sort_matriz(matriz):
    for row in matriz:
        for i in range(1, len(row)):
            key = row[i]
            j = i - 1
            while j >= 0 and key < row[j]:
                row[j + 1] = row[j]
                j -= 1
            row[j + 1] = key
    return matriz