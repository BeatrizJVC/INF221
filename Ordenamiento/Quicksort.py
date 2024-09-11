def quick_sort_arr(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_arr(left) + middle + quick_sort_arr(right)

def quick_sort(matriz):
    for i in range(len(matriz)):
        matriz[i] = quick_sort_arr(matriz[i])
    return matriz
