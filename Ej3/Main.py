from ClaseRegistro import Registro

import csv

if __name__=='__main__':
    dias = 30
    horas = 24
    lista=[]
    for i in range(horas):
        lista.append([0]*dias)
    archivo=open('archivo.csv')
    reader=csv.reader(archivo,delimiter=';')
    for linea in reader:
        dia=int(linea[0])
        hora=int(linea[1])
        temperatura=linea[2]
        humedad=linea[3]
        presatmos=linea[4]
        lista[hora][dia-1] = Registro(temperatura,humedad,presatmos)