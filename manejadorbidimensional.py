from clasecamion import camion
from clasecosecha import cosecha
import csv
class manejador:
    __listacamion = []
    __listadia = []
    __cosecha_bi = None

    def __init__(self ):
        cosecha1=cosecha()
        self.__listacamion =[]
        self.__listadia = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
        self.__cosecha_bi = cosecha1

    def cargarListaCamion(self):
        archivo=open('camiones.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            camion1 = camion(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]))
            self.__listacamion.append(camion1)

    def cargarlistacosecha(self):
        listaFinal =[]
        i = 0
        indice_dia = 0

        for i in range(20):
            listaparcial = []
            for j in range(7):
                listaparcial.append(0.0)
            listaFinal.append(listaparcial)
        id_c=int(input('\ningrese ID del camionero: '))
        while(id_c >= 1 and id_c <= 20):
            d= (input('\ningrese día:'))
            p= float(input('\n ingrese el peso del camión(kg): '))
            for i in range(len(self.__listadia)):
                if (str(self.__listadia[i]) == d):
                        indice_dia = i
            if (p > self.__listacamion[id_c].gettara()):
                listaFinal[id_c - 1][indice_dia] = p - self.__listacamion[id_c].gettara()

            id_c= int(input('Ingrese ID del camionero: '))
            i= 0
        self.__cosecha_bi.cargarbidimensional(listaFinal)


    def mostrarkilos(self, id):
        acum = 0.0
        lista = self.__cosecha_bi.getlista()
        for i in range(7):
            acum+=lista[id][i]
        return acum
    def mostrardia(self, dia):
        print( 'Patente Conductor Cantidad de kilos')
        lista = self.__cosecha_bi.getlista()
        for i in range(len(self.__listacamion)):
            print(self.__listacamion[i].getpatente(),self.__listacamion[i].getnombre(),lista[i][dia])




