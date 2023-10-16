#funcion 1
def llenado(nombre_arch):
    archivo = open(nombre_arch,"r")
    fila = len(archivo.readlines())
    archivo.seek(0)
    #matriz
    matriz = [[None]*4 for i in range(fila)]
    f=0
    for info in archivo:
        campo = info.split(" ")
        for c in range(2):
            matriz[f][c] = float(campo[c])
            if c%2 ==0:
                matriz[f][c+2] = (matriz[f][0])**2
            else:
                matriz[f][c+2] = matriz[f][c-1]* matriz[f][c]
        f += 1

    return matriz
#funcion 2
def suma(matriz):
    fila = len(matriz)
    columna = len(matriz[0])

    vector_suma = [float for i in range(columna)]
    for c in range(columna):
        s=0
        for f in range(fila):
            s += matriz[f][c]
        vector_suma[c] = s
    return vector_suma

#funcion 3
def valor_ecu(matriz0, matriz):
    n = len(matriz0)
    valores = [[None]*2 for i in range(n)]
    
    numerador_pendiente = n*matriz[3]- matriz[0]* matriz[1]
    denominador = n*matriz[2] - (matriz[0])**2
    numerador_ccte = matriz[2]*matriz[1]- matriz[3]* matriz[0]
        
    pendiente = numerador_pendiente/denominador
    ccte = numerador_ccte/denominador

    return pendiente,ccte

def final(matriz,vector_suma, valor_ecuacion):
    archivo_nuevo = open("archivonuevo.txt","w")
    fila = len(matriz)
    archivo_nuevo.write("Ecuacion de la curva de los datos obtenidos experimentalemnte\n\n")
    archivo_nuevo.write("   x        Y        x^      xy")
    archivo_nuevo.write("\n")
    for f in range(fila):
        for c in range(len(matriz[0])):
            archivo_nuevo.write(f"{matriz[f][c]:6.3f}  ")
        archivo_nuevo.write("\n")
    archivo_nuevo.write("\n\n")
    for f in range(len(vector_suma)):
        archivo_nuevo.write(f"{vector_suma[f]:6.3f}  ")
    archivo_nuevo.write("---> sumatoria columanas")
    archivo_nuevo.write("\n")
    archivo_nuevo.write("la ecuacion que mejor se ajusta para el conjunto de valores dados es: ")
    if valor_ecuacion[1]>0:
        archivo_nuevo.write(f"y(x) = {valor_ecuacion[0]:6.3f}x + {valor_ecuacion[1]:6.3f}")
    else:
        archivo_nuevo.write(f"y(x) = {valor_ecuacion[0]:6.3f}x + {valor_ecuacion[1]:6.3f}")

