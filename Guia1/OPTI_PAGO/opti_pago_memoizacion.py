def cc_billetes_dp(billetes, cantidad):
    n = len(billetes)
    
    # Inicializar la tabla dp con None
    dp = [[None] * (cantidad + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = (0, 0, [])
    
    # Rellenar la tabla dp
    for i in range(1, n + 1):
        for j in range(1, cantidad + 1):
            billete = billetes[i-1]
            
            sin_ultimo = dp[i-1][j]
            
            if j - billete >= 0:
                con_ultimo = dp[i-1][j - billete]
                if con_ultimo is not None:
                    con_ultimo = (con_ultimo[0] + 1, con_ultimo[1] + billete, con_ultimo[2] + [billete])
                else:
                    con_ultimo = None
            else:
                con_ultimo = None
        

            if con_ultimo is None:
                dp[i][j] = sin_ultimo
            elif sin_ultimo is None:
                dp[i][j] = con_ultimo
            else:
                if con_ultimo[1] < sin_ultimo[1] or (con_ultimo[1] == sin_ultimo[1] and con_ultimo[0] < sin_ultimo[0]):
                    dp[i][j] = con_ultimo
                else:
                    dp[i][j] = sin_ultimo
    
    mejor_solucion = None
    for j in range(cantidad, cantidad + 1):
        if dp[n][j] is not None:
            if mejor_solucion is None or dp[n][j][1] < mejor_solucion[1]:
                mejor_solucion = dp[n][j]
    
    return mejor_solucion

billetes = [4, 4]
cantidad = 7
resultado = cc_billetes_dp(billetes, cantidad)
if resultado:
    print(f"Cantidad de billetes: {resultado[0]}, Exceso: {resultado[1] - cantidad}, Billetes usados: {resultado[2]}")
else:
    print("No es posible alcanzar la cantidad deseada con los billetes disponibles.")
