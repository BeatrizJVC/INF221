def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    P1 = strassen(A11, restar_matrices(B12, B22))
    P2 = strassen(sumar_matrices(A11, A12), B22)
    P3 = strassen(sumar_matrices(A21, A22), B11)
    P4 = strassen(A22, restar_matrices(B21, B11))
    P5 = strassen(sumar_matrices(A11, A22), sumar_matrices(B11, B22))
    P6 = strassen(restar_matrices(A12, A22), sumar_matrices(B21, B22))
    P7 = strassen(restar_matrices(A11, A21), sumar_matrices(B11, B12))

    C11 = sumar_matrices(restar_matrices(sumar_matrices(P5, P4), P2), P6)
    C12 = sumar_matrices(P1, P2)
    C21 = sumar_matrices(P3, P4)
    C22 = restar_matrices(restar_matrices(sumar_matrices(P5, P1), P3), P7)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C
