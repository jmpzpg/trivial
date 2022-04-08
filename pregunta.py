import respuesta

class Pregunta():

    def __init__(self, id, cuerpo, dific=0, tema='general') -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__dificultad = dific
        self.__tematica = tema
        self.respuestas = [] # colección de objetos respuesta
    
    @property
    def id(self):
        return self.__id
    @property
    def cuerpo(self):
        return self.__cuerpo
    @property
    def dificultad(self):
        return self.__dificultad
    @property
    def tematica(self):
        return self.__tematica
    