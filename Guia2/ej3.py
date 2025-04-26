def potenciaLog(a,b):
    if b == 0:
        return 1
    if b % 2 == 0:
        res = potenciaLog(a, b // 2) * potenciaLog(a, b // 2)
    else:
        res = potenciaLog(a,(b-1))*a
    return res

# complejidad -> o(log n) porque en cada paso recursivo calculo la mitad de lo que tenia antes

# Probar la función con diferentes valores de a y b
print(potenciaLog(2, 10))  # Debería imprimir 1024
print(potenciaLog(3, 5))   # Debería imprimir 243
print(potenciaLog(5, 0))   # Debería imprimir 1
print(potenciaLog(7, 3))   # Debería imprimir 343
print(potenciaLog(10, 4))  # Debería imprimir 10000