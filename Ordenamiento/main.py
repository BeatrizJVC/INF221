import time
from InsertionSort import *
from Mergesort import *
from Quicksort import *
from FuncionSorting import *
from MatrizAleatoria import *
from MatrizOrden import *

def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr)
    fin = time.time()
    return fin - inicio

print("Seleccione que tipo de matriz quiere crear: \n1. Aleatoria. \n2. Aleatoria con caracteristica de orden.")
el=int(input())

if el==1:
    listam = matriz_aleatoria()
elif el==2:
    listam = matriz_orden()
else:
    print("Seleccion invalida.")

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
