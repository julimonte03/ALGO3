# Tenemos un multiconjunto B de valores de billetes y queremos comprar un producto de costo
# c de una máquina que no da vuelto. Para poder adquirir el producto debemos cubrir su costo
# usando un subconjunto de nuestros billetes. El objetivo es pagar con el mínimo exceso posible a
# fin de minimizar nuestra pérdida. Más aún, queremos gastar el menor tiempo posible poniendo
# billetes en la máquina. Por lo tanto, entre las opciones de mínimo exceso posible, queremos una
# con la menor cantidad de billetes. Por ejemplo, si c = 14 y B = {2, 3, 5, 10, 20, 20}, la solución es
# pagar 15, con exceso 1, insertando sólo dos billetes: uno de 10 y otro de 5.

def cc(billetes, cantidad):
    if cantidad <= 0:
        return (0, 0, []) 
    if not billetes:
        return None 

    ult_pos = billetes[-1]

    #usar el último billete
    con_ultimo = cc(billetes[:-1], cantidad - ult_pos)
    if con_ultimo:
        con_ultimo = (con_ultimo[0] + 1, con_ultimo[1] + ult_pos, con_ultimo[2] + [ult_pos])

    #no usar el último billete
    sin_ultimo = cc(billetes[:-1], cantidad)
    
    if not con_ultimo:
        return sin_ultimo
    if not sin_ultimo:
        return con_ultimo
    
    if con_ultimo[1] < sin_ultimo[1] or (con_ultimo[1] == sin_ultimo[1] and con_ultimo[0] < sin_ultimo[0]):
        return con_ultimo
    else:
        return sin_ultimo

billetes = [2, 3, 5, 10, 20, 20]
cantidad = 14
resultado = cc(billetes, cantidad)

if resultado:
    print(f"Cantidad de billetes: {resultado[0]}, Exceso: {resultado[1] - cantidad}, Billetes usados: {resultado[2]}")
else:
    print("No es posible encontrar una combinación de billetes adecuada.")
