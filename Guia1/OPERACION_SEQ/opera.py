def operaciones_seq(v, w):
    n = len(v)

    def f(i, x):
        if i == n:
            if x == w:
                return []
            else:
                return None
        
        # Intentar sumar
        res = f(i + 1, x + v[i])
        if res is not None:
            return ['+'] + res

        # Intentar multiplicar
        res = f(i + 1, x * v[i])
        if res is not None:
            return ['*'] + res

        # Intentar potenciar
        try:
            res = f(i + 1, x ** v[i])
            if res is not None:
                return ['^'] + res
        except OverflowError:
            # En caso de que x ** v[i] sea enorme
            pass

        return None

    return f(1, v[0])

# --- Ejemplo de uso:
v = [3, 1, 5, 2, 1]
w = 400
ops = operaciones_seq(v, w)
print(ops)
