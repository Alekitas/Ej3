class Registro:
    __temperatura=''
    __humedad=''
    __presatmos=''
    
    def __init__(self,temperatura,humedad,presatmos):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presatmos=presatmos
    def gettemperatura(self):
        return self.__temperatura