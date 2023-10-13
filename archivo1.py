def registro(arc,matriz):
    fila = len(matriz)
    vector_nombre = [[None]*2 for i in range(fila)]
    
    f = 0

    for info in arc:
        campo = info.split(",")
        
        vector_nombre[f][0],vector_nombre[f][1]=campo[0],campo[1]
        matriz[f][0] = float(campo[2])
        matriz[f][1] = float(campo[3])
        matriz[f][2] = float(campo[4])
            
        f +=1
    return vector_nombre

def prom(matriz):
    fila = len(matriz)
    vector_promedio = [None for i in range(fila)]

    for f in range(fila):
        s = 0
        for c in range(3):
            s += matriz[f][c]
        p = s/3
        vector_promedio[f] =p
    return vector_promedio


def status(promedio):
    fila = len(promedio)
    vector_estatus = [None for i in range(fila)]
    cantM = 0; cantF = 0
    for f in range(fila):
        vector_estatus[f] = "APROBADO"
        if promedio[f]<9.5:
            vector_estatus[f]= "REPROBADO"
           
    
    return vector_estatus


def final(vector_nombre,matriz,promedio,estatus):
        archivo_nuevo = open("resultado.txt", "w")
        fila = len(matriz)
        cantM = cantF = 0
        genero ="masculino"
        archivo_nuevo.write("Resumen de estudiantes" +"\n")
        archivo_nuevo.write("Nombre      g     n1      n2      n3      prom    estatus" + "\n")
        for f in range(fila):
            archivo_nuevo.write(f"{vector_nombre[f][0]:10}  {vector_nombre[f][1]}  {matriz[f][0]:6.2f}  {matriz[f][1]:6.2f}  {matriz[f][2]:6.2f}  {promedio[f]:6.2f}    {estatus[f]:10}" + "\n")
            if promedio[f]<9.5:
                if vector_nombre[f][1]=="m" or vector_nombre[f][1] =="M":
                    cantM +=1
                else:
                    cantF +=1
        if cantM<cantF:
            genero = "femenino"
        
        archivo_nuevo.write(f"el genero que reprobo mas es {genero}")

