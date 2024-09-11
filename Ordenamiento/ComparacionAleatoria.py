import time
from InsertionSort import *
from Mergesort import *
from Quicksort import *
from FuncionSorting import *
from MatrizAleatoria import *

def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr)
    fin = time.time()
    return fin - inicio

listam = matriz_aleatoria()

algoritmos = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort_matriz,
    "Quick Sort": quick_sort,
    "Sorted": sorted_matriz
}

for nombre, algoritmo in algoritmos.items():
    lista_ordenar = listam[:]
    
    tiempo = medir_tiempo(algoritmo, lista_ordenar)
    
    print(f"{nombre}: {tiempo:.6f}")
