class Registro:
    __temperatura=''
    __humedad=''
    __presatmos=''
    
    def __init__(self,temperatura,humedad,presatmos):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presatmos=presatmos
        
    def mostrarDatos(self):
        print (str(self.__temperatura)+','+str(self.__humedad)+','+str(self.__presatmos))
    def getTemperatura(self):
        return self.__temperatura
    def gethumedad(self):
        return self.__humedad
    def getpresatmos(self):
        return self.__presatmos
    
    def tempmaxima(self,lista,horas,dia):
        maximo=-9999
        for dia in range(len(lista)):
            for horas in range(len(lista[dia])):
                if lista[dia-1][horas].getTemperatura()>maximo:
                    maximo=lista[dia-1][horas].getTemperatura()
        print('Temperatura maxima: {} dia: {} hora: {}'.format(maximo,dia,horas))
    def tempminima(self,lista):
        minimo=99999
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].gettemperatura()<minimo:
                    minimo=lista[i][j].gettemperatura
                    
    def hummaxima(self,lista):
        maximo=-9999
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].gethumedad()>maximo:
                    maximo=lista[i][j].gethumedad()
    def humminima(self,lista):
        minimo=99999
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j].gethumedad()<minimo:
                    minimo=lista[i][j].gethumedad()
    def presminima(self):
        pass
    def presmaxima(self):
        pass