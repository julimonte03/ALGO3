def encontrar_mejor_subconjunto(M, k):
    n = len(M)
    mejor_suma_global = float('-inf')
    mejor_subconjunto = []

    def backtrack(indice_actual, subconjunto_parcial, suma_parcial):
        nonlocal mejor_suma_global, mejor_subconjunto

        # Caso base: tenemos un subconjunto de tamaño k
        if len(subconjunto_parcial) == k:
            if suma_parcial > mejor_suma_global:
                mejor_suma_global = suma_parcial
                mejor_subconjunto = list(subconjunto_parcial)
            return

        # Caso base: llegamos al final sin haber armado el subconjunto
        if indice_actual == n:
            return

        elementos_restantes = n - indice_actual
        faltan_elegir = k - len(subconjunto_parcial)

        # Poda: no hay suficientes elementos para completar el subconjunto
        if elementos_restantes < faltan_elegir:
            return

        # Caso 1: incluir el índice actual
        nueva_suma = suma_parcial
        for i in subconjunto_parcial:
            nueva_suma += M[indice_actual][i] + M[i][indice_actual]

        subconjunto_parcial.append(indice_actual)
        backtrack(indice_actual + 1, subconjunto_parcial, nueva_suma)
        subconjunto_parcial.pop()  # deshacer la elección

        # Caso 2: no incluir el índice actual
        backtrack(indice_actual + 1, subconjunto_parcial, suma_parcial)

    backtrack(0, [], 0)
    return mejor_suma_global, mejor_subconjunto


M = [
    [0, 10, 10, 1],
    [10, 0, 5, 2],
    [10, 5, 0, 1],
    [1, 2, 1, 0]
]

k = 3

mejor_suma, subconjunto = encontrar_mejor_subconjunto(M, k)
print("Mejor suma:", mejor_suma)
print("Subconjunto (índices desde 0):", subconjunto)
