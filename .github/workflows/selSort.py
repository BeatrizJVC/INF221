def selection_sort_matriz(matriz):
    for row in matriz:
        for i in range(len(row)):
            min_index = i
            for j in range(i + 1, len(row)):
                if row[j] < row[min_index]:
                    min_index = j
            row[i], row[min_index] = row[min_index], row[i]
    return matriz