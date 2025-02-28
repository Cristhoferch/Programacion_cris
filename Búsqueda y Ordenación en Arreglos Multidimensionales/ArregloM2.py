def ordenar_fila(matriz, fila):
    for i in range(len(matriz[fila]) - 1):
        for j in range(len(matriz[fila]) - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

matriz = [
    [3, 2, 1],
    [9, 8, 7],
    [6, 5, 4]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 0

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
for fila in matriz_ordenada:
    print(fila)
