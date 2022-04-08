class Modo():

    def __init__(self, 
                tmax_ju=600, 
                tmax_preg=60, 
                num_preg=10, 
                num_jug=1) -> None:
                
        self.__tmax_juego = tmax_ju
        self.__tmax_pregunta = tmax_preg
        self.__num_preguntas = num_preg
        self.__num_jugadores = num_jug

    @property
    def tmax_juego(self):
        return self.__tmax_juego
    @property
    def tmax_pregunta(self):
        return self.__tmax_pregunta
    @property
    def num_preguntas(self):
        return self.__num_preguntas
    @property
    def num_jugadores(self):
        return self.__num_jugadores
    
