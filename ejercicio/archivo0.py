from archivo import *
archivo = "ejercicio\TablaXY1.txt"
matriz = llenado(archivo)
v_suma = suma(matriz)
valores_ecuacion = valor_ecu(matriz, v_suma)
final(matriz, v_suma,valores_ecuacion)