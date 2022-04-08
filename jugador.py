class Jugador():

    def __init__(self, nom, res=0) -> None:
        self.__nombre = nom
        self.__resultado = res
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def resultado(self):
        return self.__resultado
    @resultado.setter
    def resultado(self, res):
        self.__resultado = res
    
