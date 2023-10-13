from archivo1 import *
#codigo principal
nombre = input("Nombre del archivo: ") + ".txt"
archivo = open(nombre,"r")
cantReg = len(archivo.readlines())
archivo.seek(0)

matriz = [[None]*3 for i in range(cantReg)]
estudiante =registro(archivo,matriz)
promedio =prom(matriz)
estatus = status(promedio)
final(estudiante,matriz,promedio,estatus)
