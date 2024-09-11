import time
import random
from Tradicional import *
from Optimizado import *
from Strassen import *
from MatricesAleatorias import *
from MatricesOrden import *

def medir_tiempo(alg, arr1, arr2):
    inicio = time.time()
    alg(arr1,arr2)
    fin = time.time()
    return fin - inicio

def crear_mats():
    print("IMPORTANTE: El valor de la columna de matriz 1 debe ser igual al valor de fila de matriz 2 y los tamaños deben ser potencias de 2.")
    listasm = matrices_orden()
    return listasm


algoritmos = {
    "Tradicional": tradicional,
    "Optimizado": optimizado,
    "Strassen": strassen
}

listasf=crear_mats()
lista1=listasf[0]
lista2=listasf[1]

for nombre, algoritmo in algoritmos.items():
    lista_1 = lista1[:]
    lista_2 = lista2[:]

    tiempo = medir_tiempo(algoritmo, lista_1, lista_2)

    print(f"{nombre}: {tiempo:.6f}")
